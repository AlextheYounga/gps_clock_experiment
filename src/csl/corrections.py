"""CSL correction terms.

This module isolates correction math used by the CSL model so those
assumptions are explicit and easy to compare against VSL.
"""

from __future__ import annotations

import math

from src.constants import F_RELATIVISTIC, OMEGA_E_DOT_RAD_S, SPEED_OF_LIGHT_MPS
from src.models import Ephemeris


def polynomial_clock_correction_s(ephemeris: Ephemeris, tc_s: float) -> float:
    """Return broadcast polynomial clock correction (seconds)."""
    return ephemeris.af0 + ephemeris.af1 * tc_s + ephemeris.af2 * tc_s * tc_s - ephemeris.tgd


def relativistic_eccentricity_correction_s(ephemeris: Ephemeris, eccentric_anomaly_rad: float) -> float:
    """Return CSL relativistic eccentricity clock correction (seconds)."""
    return F_RELATIVISTIC * ephemeris.e * ephemeris.root_a * math.sin(eccentric_anomaly_rad)


def sagnac_style_orbit_longitude_rad(ephemeris: Ephemeris, tk_s: float, user_sat_range_m: float) -> float:
    """Return standard Sagnac-style orbit longitude term used by CSL."""
    return (
        ephemeris.omega0
        + (ephemeris.omega_dot - OMEGA_E_DOT_RAD_S) * tk_s
        - OMEGA_E_DOT_RAD_S * (ephemeris.toe + user_sat_range_m / SPEED_OF_LIGHT_MPS)
    )
