"""CSL satellite orbit computation (ICD-GPS-200 broadcast orbit model).

Computes ECEF satellite position from Keplerian elements, including
the standard Sagnac / Earth-rotation longitude correction.

This module belongs entirely to the CSL package.
"""

from __future__ import annotations

import math

from src.constants import MU_M3_S2, OMEGA_E_DOT_RAD_S, SECONDS_IN_WEEK, SPEED_OF_LIGHT_MPS
from src.models import Ephemeris

from src.csl.clock import SatClockCorrection, calculate_clock_correction
from src.csl.config import CslConfig

_SAT_POSITION_ITERATIONS = 5


def _satellite_position_inner(
    ephemeris: Ephemeris,
    sat_clock: SatClockCorrection,
    user_sat_range_m: float,
) -> tuple[float, float, float]:
    """Compute one ECEF position from orbit elements given pre-solved clock state."""
    e = sat_clock.eccentric_anomaly_rad
    tk_s = sat_clock.time_from_ref_epoch_s

    true_anom = math.atan2(
        math.sqrt(1.0 - ephemeris.e * ephemeris.e) * math.sin(e),
        math.cos(e) - ephemeris.e,
    )

    u = true_anom + ephemeris.omega
    r = ephemeris.root_a * ephemeris.root_a * (1.0 - ephemeris.e * math.cos(e))

    sin_2u = math.sin(2.0 * u)
    cos_2u = math.cos(2.0 * u)

    r += ephemeris.crc * cos_2u + ephemeris.crs * sin_2u
    u += ephemeris.cuc * cos_2u + ephemeris.cus * sin_2u
    inc = ephemeris.i0 + ephemeris.i_dot * tk_s + ephemeris.cic * cos_2u + ephemeris.cis * sin_2u

    x_orb = r * math.cos(u)
    y_orb = r * math.sin(u)

    omega_k = (
        ephemeris.omega0
        + (ephemeris.omega_dot - OMEGA_E_DOT_RAD_S) * tk_s
        - OMEGA_E_DOT_RAD_S * (ephemeris.toe + user_sat_range_m / SPEED_OF_LIGHT_MPS)
    )

    cos_ok = math.cos(omega_k)
    sin_ok = math.sin(omega_k)
    cos_i = math.cos(inc)

    sx = x_orb * cos_ok - y_orb * cos_i * sin_ok
    sy = x_orb * sin_ok + y_orb * cos_i * cos_ok
    sz = y_orb * math.sin(inc)
    return sx, sy, sz


def calculate_satellite_position(
    ephemeris: Ephemeris,
    corrected_tow_s: float,
    week: int,
    user_pos_xyz_m: tuple[float, float, float],
    config: CslConfig,
) -> tuple[float, float, float]:
    """Compute ECEF satellite position, iterating the range estimate for Sagnac."""
    user_sat_range_m = 0.070 * SPEED_OF_LIGHT_MPS
    sx = sy = sz = 0.0

    for _ in range(_SAT_POSITION_ITERATIONS):
        sat_clock = calculate_clock_correction(ephemeris, corrected_tow_s, week, config)
        sx, sy, sz = _satellite_position_inner(ephemeris, sat_clock, user_sat_range_m)
        dx = sx - user_pos_xyz_m[0]
        dy = sy - user_pos_xyz_m[1]
        dz = sz - user_pos_xyz_m[2]
        user_sat_range_m = math.sqrt(dx * dx + dy * dy + dz * dz)

    return sx, sy, sz
