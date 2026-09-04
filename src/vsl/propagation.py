"""VSL ballistic signal propagation.

Implements the full-vector ballistic propagation model:

  v_sig = c_emit * u_aim + v_sat

where the emitted signal inherits the satellite's inertial velocity.
For fixed satellite/receiver geometry, the flight time is solved exactly
from the ballistic interception constraint:

  |dr - v_sat * dt|^2 = c_eff^2 * dt^2

with dr = r_rcv - r_sat.
The receiver is modelled as moving with the rotating Earth during signal
flight, so dr depends on dt via receiver rotation and is refined iteratively.

No standard constant-c propagation assumption is layered on top.
No Sagnac add-on correction is used: Earth rotation enters only through
the receiver's physical motion during the flight time.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from src.constants import SECONDS_IN_WEEK, SPEED_OF_LIGHT_MPS as EMISSION_SPEED_MPS
from src.models import Ephemeris
from src.vsl.clock import calculate_clock_correction
from src.vsl.corrections import (
    earth_rotation_velocity_mps,
    ecef_to_inertial_velocity_mps,
    gravity_adjusted_emission_speed_mps,
    rotate_ecef_position_forward,
)
from src.vsl.orbit import calculate_satellite_state

_BALLISTIC_FLIGHT_ITERATIONS = 15
_FLIGHT_TIME_TOLERANCE_S = 1.0e-14


@dataclass(frozen=True)
class BallisticObsDebug:
    """Per-observation diagnostics from the ballistic propagation solve."""

    flight_time_s: float
    """Signal flight time under the ballistic model (seconds)."""

    sat_vel_magnitude_mps: float
    """Satellite speed in the transmit-time inertial basis (m/s)."""

    sat_vel_ecef_magnitude_mps: float
    """Satellite speed returned by the broadcast ECEF orbit model (m/s)."""

    earth_rotation_velocity_magnitude_mps: float
    """Magnitude of the restored omega x r satellite velocity term (m/s)."""

    sat_vel_along_los_mps: float
    """Satellite velocity projected onto the signal line-of-sight (m/s).
    Positive = satellite moving toward receiver."""

    rcv_vel_along_los_mps: float
    """Receiver rotational velocity projected onto the signal line-of-sight (m/s).
    Positive = receiver moving toward satellite."""

    predicted_pseudorange_m: float
    """Predicted pseudorange from the ballistic model (m)."""

    sat_clock_polynomial_m: float
    """Broadcast polynomial satellite clock correction component (m)."""

    sat_clock_gravity_periodic_m: float
    """Gravity-only periodic eccentricity clock correction component (m)."""

    gravity_prop_delta_c_mps: float
    """Gravity-induced propagation-speed shift relative to c_emit (m/s)."""

    transmit_time_shift_s: float
    """Ballistic transmit-time change relative to the pseudorange/c bootstrap."""


def _subtract_flight_time(tow_s: float, week: int, flight_time_s: float) -> tuple[float, int]:
    """Return GPS TOW/week at transmission after subtracting flight time."""
    transmit_tow_s = tow_s - flight_time_s
    if transmit_tow_s < 0.0:
        return transmit_tow_s + SECONDS_IN_WEEK, week - 1
    return transmit_tow_s, week


def _add_clock_correction(tow_s: float, week: int, correction_s: float) -> tuple[float, int]:
    """Return GPS TOW/week after applying a satellite clock correction."""
    corrected_tow_s = tow_s + correction_s
    if corrected_tow_s >= SECONDS_IN_WEEK:
        return corrected_tow_s - SECONDS_IN_WEEK, week + 1
    if corrected_tow_s < 0.0:
        return corrected_tow_s + SECONDS_IN_WEEK, week - 1
    return corrected_tow_s, week


def compute_predicted_pseudorange(  # noqa: PLR0915
    ephemeris: Ephemeris,
    receiver_tow_corrected_s: float,
    gps_week: int,
    pseudorange_m: float,
    user_state: np.ndarray,
) -> tuple[float, BallisticObsDebug]:
    """Compute predicted pseudorange under the ballistic full-vector model.

    Returns (predicted_pseudorange_m, BallisticObsDebug).

    The receiver is rotated from reception into the transmit-time-oriented
    inertial basis. The ECEF satellite velocity is converted to that same
    basis with ``v_inertial = v_ecef + omega_earth x r_sat``. Transmit time,
    satellite state, and flight time are iterated together.

    The receiver measures time-of-flight * c_emit regardless of signal speed,
    so the output pseudorange is expressed in metres via c_emit * flight_time.
    """
    c_emit = EMISSION_SPEED_MPS
    user_xyz = (float(user_state[0]), float(user_state[1]), float(user_state[2]))
    clock_bias_m = float(user_state[3])

    rcv_pos = np.array(user_xyz)
    bootstrap_flight_time_s = pseudorange_m / c_emit
    flight_time = bootstrap_flight_time_s
    u_aim = np.zeros(3)
    sat_clock_corr_m = 0.0
    sat_clock_poly_m = 0.0
    sat_clock_gravity_periodic_m = 0.0
    sat_pos = np.zeros(3)
    sat_vel_ecef = np.zeros(3)
    sat_vel_inertial = np.zeros(3)
    rcv_at_rx = rcv_pos
    c_eff = c_emit

    for _ in range(_BALLISTIC_FLIGHT_ITERATIONS):
        tow_tx, tx_week = _subtract_flight_time(receiver_tow_corrected_s, gps_week, flight_time)
        clock_corr = calculate_clock_correction(ephemeris, tow_tx, tx_week)
        sat_clock_corr_m = clock_corr.satellite_clock_correction_m
        sat_clock_poly_m = clock_corr.polynomial_correction_s * c_emit
        sat_clock_gravity_periodic_m = clock_corr.gravity_periodic_correction_s * c_emit
        corrected_tx, corrected_week = _add_clock_correction(
            tow_tx,
            tx_week,
            sat_clock_corr_m / c_emit,
        )
        sat_state = calculate_satellite_state(ephemeris, corrected_tx, corrected_week)
        sat_pos = np.array(sat_state.pos_m)
        sat_vel_ecef = np.array(sat_state.vel_mps)
        sat_vel_inertial = np.array(ecef_to_inertial_velocity_mps(sat_state.pos_m, sat_state.vel_mps))
        rcv_at_rx = np.array(rotate_ecef_position_forward(user_xyz, flight_time))
        dr = rcv_at_rx - sat_pos
        d = float(np.dot(dr, dr))
        if d < 1.0:
            raise RuntimeError("Degenerate satellite-receiver geometry")

        sat_radius_m = float(np.linalg.norm(sat_pos))
        rcv_radius_m = float(np.linalg.norm(rcv_at_rx))
        c_eff = gravity_adjusted_emission_speed_mps(sat_radius_m, rcv_radius_m)

        # Ballistic interception quadratic (for fixed dr geometry):
        #   |dr - v_sat * dt|^2 = c_eff^2 * dt^2
        # -> a*dt^2 + b*dt + d = 0
        #   a = |v_sat_inertial|^2 - c_eff^2, b = -2*(dr.v_sat_inertial), d = |dr|^2
        a = float(np.dot(sat_vel_inertial, sat_vel_inertial) - c_eff * c_eff)
        b = float(-2.0 * np.dot(dr, sat_vel_inertial))
        discriminant = b * b - 4.0 * a * d
        if discriminant < 0.0:
            raise RuntimeError("Ballistic interception has no real flight-time solution")

        sqrt_disc = math.sqrt(discriminant)
        denom = 2.0 * a
        dt1 = (-b + sqrt_disc) / denom
        dt2 = (-b - sqrt_disc) / denom
        positive_roots = [dt for dt in (dt1, dt2) if dt > 0.0 and math.isfinite(dt)]
        if not positive_roots:
            raise RuntimeError("Ballistic interception has no positive flight-time solution")

        new_ft = min(positive_roots)

        if abs(new_ft - flight_time) < _FLIGHT_TIME_TOLERANCE_S:
            flight_time = new_ft
            break
        flight_time = new_ft
    else:
        raise RuntimeError("Ballistic transmit-time solve did not converge")

    # Refresh the state at the converged transmit time before emitting diagnostics.
    tow_tx, tx_week = _subtract_flight_time(receiver_tow_corrected_s, gps_week, flight_time)
    clock_corr = calculate_clock_correction(ephemeris, tow_tx, tx_week)
    sat_clock_corr_m = clock_corr.satellite_clock_correction_m
    sat_clock_poly_m = clock_corr.polynomial_correction_s * c_emit
    sat_clock_gravity_periodic_m = clock_corr.gravity_periodic_correction_s * c_emit
    corrected_tx, corrected_week = _add_clock_correction(tow_tx, tx_week, sat_clock_corr_m / c_emit)
    sat_state = calculate_satellite_state(ephemeris, corrected_tx, corrected_week)
    sat_pos = np.array(sat_state.pos_m)
    sat_vel_ecef = np.array(sat_state.vel_mps)
    sat_vel_inertial = np.array(ecef_to_inertial_velocity_mps(sat_state.pos_m, sat_state.vel_mps))
    rcv_at_rx = np.array(rotate_ecef_position_forward(user_xyz, flight_time))
    dr = rcv_at_rx - sat_pos
    c_eff = gravity_adjusted_emission_speed_mps(float(np.linalg.norm(sat_pos)), float(np.linalg.norm(rcv_at_rx)))
    u_aim = (dr / flight_time - sat_vel_inertial) / c_eff
    u_aim_norm = float(np.linalg.norm(u_aim))
    if u_aim_norm > 0.0:
        u_aim = u_aim / u_aim_norm

    rcv_vel = np.array(earth_rotation_velocity_mps(tuple(rcv_at_rx)))

    # Project velocities onto ballistic emission direction.
    sat_vel_along_los = float(np.dot(sat_vel_inertial, u_aim)) if np.any(u_aim) else 0.0
    # Receiver velocity positive toward satellite means negative along u_aim
    rcv_vel_along_los = -float(np.dot(rcv_vel, u_aim)) if np.any(u_aim) else 0.0

    # Step 5: predicted pseudorange expressed via c_emit * flight_time
    predicted_pr = flight_time * c_emit - sat_clock_corr_m + clock_bias_m

    gravity_prop_delta_c_mps = c_eff - c_emit
    earth_rotation_velocity_magnitude_mps = float(
        np.linalg.norm(np.array(earth_rotation_velocity_mps(sat_state.pos_m)))
    )

    debug = BallisticObsDebug(
        flight_time_s=flight_time,
        sat_vel_magnitude_mps=float(np.linalg.norm(sat_vel_inertial)),
        sat_vel_ecef_magnitude_mps=float(np.linalg.norm(sat_vel_ecef)),
        earth_rotation_velocity_magnitude_mps=earth_rotation_velocity_magnitude_mps,
        sat_vel_along_los_mps=sat_vel_along_los,
        rcv_vel_along_los_mps=rcv_vel_along_los,
        predicted_pseudorange_m=predicted_pr,
        sat_clock_polynomial_m=sat_clock_poly_m,
        sat_clock_gravity_periodic_m=sat_clock_gravity_periodic_m,
        gravity_prop_delta_c_mps=gravity_prop_delta_c_mps,
        transmit_time_shift_s=bootstrap_flight_time_s - flight_time,
    )
    return predicted_pr, debug
