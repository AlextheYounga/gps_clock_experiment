"""VSL observation model: residuals and geometry matrix.

All pseudorange prediction in this module uses the VSL ballistic
propagation model. No CSL / constant-c propagation helpers are imported.

The geometry (H) matrix uses satellite positions from the VSL orbit module
for linearization. These positions are computed with the same broadcast
Keplerian model but without the standard Sagnac correction, consistent
with the ballistic propagation framework.
"""

from __future__ import annotations

import math

import numpy as np

from src.constants import SECONDS_IN_WEEK, SPEED_OF_LIGHT_MPS
from src.ephemeris_selection import select_ephemeris
from src.models import Ephemeris, SatelliteObservation
from src.vsl.clock import calculate_clock_correction
from src.vsl.orbit import calculate_satellite_position
from src.vsl.propagation import BallisticObsDebug, compute_predicted_pseudorange


def compute_residuals(
    observations: list[SatelliteObservation],
    receiver_tow_s: float,
    gps_week: int,
    nav_by_prn: dict[int, list[Ephemeris]],
    state: np.ndarray,
) -> tuple[np.ndarray, list[tuple[float, float, float]], list[int], list[BallisticObsDebug]]:
    """Compute observation residuals under the VSL ballistic model.

    Returns (residuals_m, sat_positions_for_H_matrix, sat_ids, obs_debug).
    """
    residuals: list[float] = []
    sat_positions: list[tuple[float, float, float]] = []
    sat_ids: list[int] = []
    obs_debug: list[BallisticObsDebug] = []

    c = SPEED_OF_LIGHT_MPS
    tow_corrected = receiver_tow_s - state[3] / c
    user_pos = (float(state[0]), float(state[1]), float(state[2]))

    for obs in observations:
        eph = select_ephemeris(nav_by_prn[obs.svid], tow_corrected, gps_week)

        # Predicted pseudorange from ballistic propagation
        predicted_pr, debug = compute_predicted_pseudorange(
            eph,
            tow_corrected,
            gps_week,
            obs.pseudorange_m,
            state,
        )
        residuals.append(obs.pseudorange_m - predicted_pr)
        obs_debug.append(debug)

        # Satellite position for H-matrix (VSL orbit, no Sagnac)
        # Use initial transmit-time estimate consistent with observation
        tow_tx = tow_corrected - obs.pseudorange_m / c
        week_tx = gps_week
        if tow_tx < 0.0:
            tow_tx += SECONDS_IN_WEEK
            week_tx -= 1
        elif tow_tx > SECONDS_IN_WEEK:
            tow_tx -= SECONDS_IN_WEEK
            week_tx += 1

        clock_corr = calculate_clock_correction(eph, tow_tx, week_tx)
        corrected_tx = tow_tx + clock_corr.satellite_clock_correction_m / c
        if corrected_tx < 0.0:
            corrected_tx += SECONDS_IN_WEEK
            week_tx -= 1
        elif corrected_tx > SECONDS_IN_WEEK:
            corrected_tx -= SECONDS_IN_WEEK
            week_tx += 1

        sat_pos = calculate_satellite_position(eph, corrected_tx, week_tx, user_pos)
        sat_positions.append(sat_pos)
        sat_ids.append(obs.svid)

    return np.array(residuals, dtype=float), sat_positions, sat_ids, obs_debug


def geometry_matrix(
    sat_positions: list[tuple[float, float, float]],
    state: np.ndarray,
) -> np.ndarray:
    """Build the linearized geometry (H) matrix for WLS."""
    h = np.zeros((len(sat_positions), 4), dtype=float)
    for i, sat_pos in enumerate(sat_positions):
        dx = sat_pos[0] - state[0]
        dy = sat_pos[1] - state[1]
        dz = sat_pos[2] - state[2]
        norm = math.sqrt(dx * dx + dy * dy + dz * dz)
        h[i, 0] = (state[0] - sat_pos[0]) / norm
        h[i, 1] = (state[1] - sat_pos[1]) / norm
        h[i, 2] = (state[2] - sat_pos[2]) / norm
        h[i, 3] = 1.0
    return h
