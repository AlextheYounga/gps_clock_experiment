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

from src.constants import OMEGA_E_DOT_RAD_S, SECONDS_IN_WEEK, SPEED_OF_LIGHT_MPS as EMISSIONS_SPEED_OF_LIGHT_MPS
from src.models import Ephemeris
from src.vsl.clock import calculate_clock_correction
from src.vsl.corrections import gravity_adjusted_emission_speed_mps
from src.vsl.orbit import calculate_satellite_state

_BALLISTIC_FLIGHT_ITERATIONS = 10
_FLIGHT_TIME_TOLERANCE_S = 1.0e-14


@dataclass(frozen=True)
class BallisticObsDebug:
    """Per-observation diagnostics from the ballistic propagation solve."""

    flight_time_s: float
    """Signal flight time under the ballistic model (seconds)."""

    sat_vel_magnitude_mps: float
    """Satellite speed in the inertial frame (m/s)."""

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


def _rotate_receiver_by_dt(
    rcv_ecef: tuple[float, float, float],
    dt_s: float,
) -> tuple[float, float, float]:
    """Rotate receiver ECEF position forward by Earth rotation over dt_s."""
    angle = OMEGA_E_DOT_RAD_S * dt_s
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    x = rcv_ecef[0] * cos_a - rcv_ecef[1] * sin_a
    y = rcv_ecef[0] * sin_a + rcv_ecef[1] * cos_a
    z = rcv_ecef[2]
    return x, y, z


def compute_predicted_pseudorange(  # noqa: C901, PLR0915
    ephemeris: Ephemeris,
    receiver_tow_corrected_s: float,
    gps_week: int,
    pseudorange_m: float,
    user_state: np.ndarray,
) -> tuple[float, BallisticObsDebug]:
    """Compute predicted pseudorange under the ballistic full-vector model.

    Returns (predicted_pseudorange_m, BallisticObsDebug).

    Algorithm:
    1. Initial transmit-time estimate using pseudorange / c as a bootstrap.
    2. Apply VSL satellite clock correction (polynomial + gravity-only periodic term).
    3. Get satellite ECEF state (position + velocity) at corrected transmit time.
    4. Iterate Earth-rotation geometry and solve flight time exactly each pass:
         |dr - v_sat * dt|^2 = c_eff^2 * dt^2
       where dr = r_rcv(t_rx) - r_sat(t_tx) and r_rcv(t_rx) is rotated
       forward by dt on each iteration. The effective emission speed is
       reduced slightly by the path-averaged Earth gravitational potential.
    5. predicted_pseudorange = flight_time * c_emit - sat_clock_corr_m + clock_bias_m

    The receiver measures time-of-flight * c_emit regardless of signal speed,
    so the output pseudorange is expressed in metres via c_emit * flight_time.
    """
    c_emit = EMISSIONS_SPEED_OF_LIGHT_MPS
    user_xyz = (float(user_state[0]), float(user_state[1]), float(user_state[2]))
    clock_bias_m = float(user_state[3])

    # Step 1: initial transmit time (constant-c bootstrap)
    tow_tx = receiver_tow_corrected_s - pseudorange_m / c_emit
    week = gps_week
    if tow_tx < 0.0:
        tow_tx += SECONDS_IN_WEEK
        week -= 1
    elif tow_tx > SECONDS_IN_WEEK:
        tow_tx -= SECONDS_IN_WEEK
        week += 1

    # Step 2: VSL clock correction (polynomial only)
    clock_corr = calculate_clock_correction(ephemeris, tow_tx, week)
    sat_clock_corr_m = clock_corr.satellite_clock_correction_m
    sat_clock_poly_m = clock_corr.polynomial_correction_s * c_emit
    sat_clock_gravity_periodic_m = clock_corr.gravity_periodic_correction_s * c_emit

    corrected_tx = tow_tx + sat_clock_corr_m / c_emit
    if corrected_tx < 0.0:
        corrected_tx += SECONDS_IN_WEEK
        week -= 1
    elif corrected_tx > SECONDS_IN_WEEK:
        corrected_tx -= SECONDS_IN_WEEK
        week += 1

    # Step 3: satellite state at transmit time
    sat_state = calculate_satellite_state(ephemeris, corrected_tx, week)
    sat_pos = np.array(sat_state.pos_m)
    sat_vel = np.array(sat_state.vel_mps)

    # Step 4: iterate Earth-rotation geometry with exact ballistic dt solve
    rcv_pos = np.array(user_xyz)
    flight_time = np.linalg.norm(sat_pos - rcv_pos) / c_emit  # initial guess
    u_aim = np.zeros(3)

    for _ in range(_BALLISTIC_FLIGHT_ITERATIONS):
        rcv_at_rx = np.array(_rotate_receiver_by_dt(user_xyz, flight_time))
        dr = rcv_at_rx - sat_pos
        d = float(np.dot(dr, dr))
        if d < 1.0:
            break

        sat_radius_m = float(np.linalg.norm(sat_pos))
        rcv_radius_m = float(np.linalg.norm(rcv_at_rx))
        c_eff = gravity_adjusted_emission_speed_mps(sat_radius_m, rcv_radius_m)

        # Ballistic interception quadratic (for fixed dr geometry):
        #   |dr - v_sat * dt|^2 = c_eff^2 * dt^2
        # -> a*dt^2 + b*dt + d = 0
        #   a = |v_sat|^2 - c_eff^2, b = -2*(dr.v_sat), d = |dr|^2
        a = float(np.dot(sat_vel, sat_vel) - c_eff * c_eff)
        b = float(-2.0 * np.dot(dr, sat_vel))
        discriminant = b * b - 4.0 * a * d
        if discriminant < 0.0:
            break

        sqrt_disc = math.sqrt(discriminant)
        denom = 2.0 * a
        dt1 = (-b + sqrt_disc) / denom
        dt2 = (-b - sqrt_disc) / denom
        positive_roots = [dt for dt in (dt1, dt2) if dt > 0.0 and math.isfinite(dt)]
        if not positive_roots:
            break

        new_ft = min(positive_roots)

        if abs(new_ft - flight_time) < _FLIGHT_TIME_TOLERANCE_S:
            flight_time = new_ft
            break
        flight_time = new_ft

    # Emission direction in satellite frame from converged geometry.
    if flight_time > 0.0:
        rcv_at_rx = np.array(_rotate_receiver_by_dt(user_xyz, flight_time))
        dr = rcv_at_rx - sat_pos
        sat_radius_m = float(np.linalg.norm(sat_pos))
        rcv_radius_m = float(np.linalg.norm(rcv_at_rx))
        c_eff = gravity_adjusted_emission_speed_mps(sat_radius_m, rcv_radius_m)
        u_aim = (dr / flight_time - sat_vel) / c_eff
        u_aim_norm = float(np.linalg.norm(u_aim))
        if u_aim_norm > 0.0:
            u_aim = u_aim / u_aim_norm

    # Compute receiver rotational velocity in ECEF (omega x r)
    # v_rcv = omega_E x r_rcv  (z-component only for Earth rotation)
    rx, ry = float(user_state[0]), float(user_state[1])
    rcv_vel = np.array([-OMEGA_E_DOT_RAD_S * ry, OMEGA_E_DOT_RAD_S * rx, 0.0])

    # Project velocities onto ballistic emission direction.
    sat_vel_along_los = float(np.dot(sat_vel, u_aim)) if np.any(u_aim) else 0.0
    # Receiver velocity positive toward satellite means negative along u_aim
    rcv_vel_along_los = -float(np.dot(rcv_vel, u_aim)) if np.any(u_aim) else 0.0

    # Step 5: predicted pseudorange expressed via c_emit * flight_time
    predicted_pr = flight_time * c_emit - sat_clock_corr_m + clock_bias_m

    rcv_at_rx_final = np.array(_rotate_receiver_by_dt(user_xyz, flight_time))
    c_eff_final = gravity_adjusted_emission_speed_mps(
        float(np.linalg.norm(sat_pos)),
        float(np.linalg.norm(rcv_at_rx_final)),
    )
    gravity_prop_delta_c_mps = c_eff_final - c_emit

    debug = BallisticObsDebug(
        flight_time_s=flight_time,
        sat_vel_magnitude_mps=float(np.linalg.norm(sat_vel)),
        sat_vel_along_los_mps=sat_vel_along_los,
        rcv_vel_along_los_mps=rcv_vel_along_los,
        predicted_pseudorange_m=predicted_pr,
        sat_clock_polynomial_m=sat_clock_poly_m,
        sat_clock_gravity_periodic_m=sat_clock_gravity_periodic_m,
        gravity_prop_delta_c_mps=gravity_prop_delta_c_mps,
    )
    return predicted_pr, debug
