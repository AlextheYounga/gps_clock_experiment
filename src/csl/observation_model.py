"""CSL observation model: residuals and geometry matrix.

Computes predicted pseudoranges and observation residuals under the
constant-speed-light assumption. All transmit-time and pseudorange
prediction logic in this module is CSL-specific.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from src.constants import OMEGA_E_DOT_RAD_S, SPEED_OF_LIGHT_MPS
from src.csl.clock import calculate_clock_correction, calculate_corrected_transmit_tow_and_week
from src.csl.config import CslConfig
from src.csl.orbit import calculate_satellite_position
from src.ephemeris_selection import select_ephemeris
from src.models import Ephemeris, SatelliteObservation


@dataclass(frozen=True)
class CslObsDebug:
    """Per-observation correction diagnostics under CSL."""

    sat_clock_polynomial_m: float
    sat_clock_rel_eccentricity_m: float
    sagnac_equivalent_range_m: float


def compute_residuals(  # noqa: PLR0913
    observations: list[SatelliteObservation],
    receiver_tow_s: float,
    gps_week: int,
    nav_by_prn: dict[int, list[Ephemeris]],
    state: np.ndarray,
    config: CslConfig,
) -> tuple[np.ndarray, list[tuple[float, float, float]], list[int], list[CslObsDebug]]:
    """Compute observation residuals under the CSL model.

    Returns (residuals_m, sat_positions, sat_ids, obs_debug).
    """
    residuals: list[float] = []
    sat_positions: list[tuple[float, float, float]] = []
    sat_ids: list[int] = []
    obs_debug: list[CslObsDebug] = []

    user_pos = (float(state[0]), float(state[1]), float(state[2]))
    tow_corrected = receiver_tow_s - state[3] / SPEED_OF_LIGHT_MPS

    for obs in observations:
        eph = select_ephemeris(nav_by_prn[obs.svid], tow_corrected, gps_week)

        tx_tow, tx_week = calculate_corrected_transmit_tow_and_week(
            eph,
            tow_corrected,
            gps_week,
            obs.pseudorange_m,
            config,
        )

        sat_pos = calculate_satellite_position(eph, tx_tow, tx_week, user_pos, config)

        sat_clock = calculate_clock_correction(
            eph,
            tx_tow,
            tx_week,
            config,
        )
        sat_clock_corr_m = sat_clock.satellite_clock_correction_m

        dx = sat_pos[0] - state[0]
        dy = sat_pos[1] - state[1]
        dz = sat_pos[2] - state[2]
        geometric_range_m = math.sqrt(dx * dx + dy * dy + dz * dz)
        predicted_pr = geometric_range_m - sat_clock_corr_m + state[3]

        sagnac_equiv_m = OMEGA_E_DOT_RAD_S / SPEED_OF_LIGHT_MPS * (sat_pos[0] * state[1] - sat_pos[1] * state[0])

        residuals.append(obs.pseudorange_m - predicted_pr)
        sat_positions.append(sat_pos)
        sat_ids.append(obs.svid)
        obs_debug.append(
            CslObsDebug(
                sat_clock_polynomial_m=sat_clock.polynomial_correction_s * SPEED_OF_LIGHT_MPS,
                sat_clock_rel_eccentricity_m=sat_clock.relativistic_correction_s * SPEED_OF_LIGHT_MPS,
                sagnac_equivalent_range_m=sagnac_equiv_m,
            )
        )

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
