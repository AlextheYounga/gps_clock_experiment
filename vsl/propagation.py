"""VSL ballistic signal propagation.

Implements the full-vector ballistic propagation model:

  v_sig = c * u_emit + v_sat

where the emitted signal inherits the satellite's inertial velocity.
The receiver is modelled as moving with the rotating Earth during signal
flight, so arrival is solved as an interception problem:

  r_sat(t_tx) + v_sig * dt = r_rcv(t_rx)

No standard constant-c propagation assumption is layered on top.
No Sagnac add-on correction is used: Earth rotation enters only through
the receiver's physical motion during the flight time.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from src.constants import OMEGA_E_DOT_RAD_S, SECONDS_IN_WEEK, SPEED_OF_LIGHT_MPS
from src.models import Ephemeris

from vsl.clock import calculate_clock_correction
from vsl.orbit import calculate_satellite_state

_BALLISTIC_FLIGHT_ITERATIONS = 10


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


def compute_predicted_pseudorange(
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
    2. Apply VSL satellite clock correction (polynomial only, no rel. term).
    3. Get satellite ECEF state (position + velocity) at corrected transmit time.
    4. Iterate the ballistic flight time:
         v_sig = c * u_emit + v_sat
         flight_time = |dr| / (v_sig . u_emit)
       where dr = r_rcv(t_rx) - r_sat(t_tx) and the receiver is rotated
       forward by flight_time on each iteration.
    5. predicted_pseudorange = flight_time * c - sat_clock_corr_m + clock_bias_m

    The receiver measures time-of-flight * c regardless of signal speed, so
    the output pseudorange is expressed in metres via c * flight_time.
    """
    c = SPEED_OF_LIGHT_MPS
    user_xyz = (float(user_state[0]), float(user_state[1]), float(user_state[2]))
    clock_bias_m = float(user_state[3])

    # Step 1: initial transmit time (constant-c bootstrap)
    tow_tx = receiver_tow_corrected_s - pseudorange_m / c
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

    corrected_tx = tow_tx + sat_clock_corr_m / c
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

    # Step 4: iterate ballistic flight time
    rcv_pos = np.array(user_xyz)
    flight_time = np.linalg.norm(sat_pos - rcv_pos) / c  # initial guess
    u_emit = np.zeros(3)

    for _ in range(_BALLISTIC_FLIGHT_ITERATIONS):
        rcv_at_rx = np.array(_rotate_receiver_by_dt(user_xyz, flight_time))
        dr = rcv_at_rx - sat_pos
        dist = float(np.linalg.norm(dr))
        if dist < 1.0:
            break
        u_emit = dr / dist

        # Ballistic signal speed along line of sight
        v_along_los = c + float(np.dot(sat_vel, u_emit))
        if v_along_los <= 0.0:
            break

        new_ft = dist / v_along_los
        if abs(new_ft - flight_time) < 1e-14:
            break
        flight_time = new_ft

    # Compute receiver rotational velocity in ECEF (omega x r)
    # v_rcv = omega_E x r_rcv  (z-component only for Earth rotation)
    rx, ry, rz = float(user_state[0]), float(user_state[1]), float(user_state[2])
    rcv_vel = np.array([-OMEGA_E_DOT_RAD_S * ry, OMEGA_E_DOT_RAD_S * rx, 0.0])

    # Project velocities onto LOS (u_emit points sat→rcv, so positive = toward rcv)
    sat_vel_along_los = float(np.dot(sat_vel, u_emit)) if np.any(u_emit) else 0.0
    # Receiver velocity positive toward satellite means negative along u_emit
    rcv_vel_along_los = -float(np.dot(rcv_vel, u_emit)) if np.any(u_emit) else 0.0

    # Step 5: predicted pseudorange expressed via c * flight_time
    predicted_pr = flight_time * c - sat_clock_corr_m + clock_bias_m

    debug = BallisticObsDebug(
        flight_time_s=flight_time,
        sat_vel_magnitude_mps=float(np.linalg.norm(sat_vel)),
        sat_vel_along_los_mps=sat_vel_along_los,
        rcv_vel_along_los_mps=rcv_vel_along_los,
        predicted_pseudorange_m=predicted_pr,
    )
    return predicted_pr, debug
