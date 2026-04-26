"""VSL correction terms.

This module isolates correction math used by the VSL clock model so the
experimental assumptions can be changed in one place.
"""

from __future__ import annotations

import math

from src.constants import (
    F_RELATIVISTIC,
    OMEGA_E_DOT_RAD_S,
    SPEED_OF_LIGHT_MPS as EMISSIONS_SPEED_OF_LIGHT_MPS,
)
from src.models import Ephemeris


def polynomial_clock_correction_s(ephemeris: Ephemeris, tc_s: float) -> float:
    """Return broadcast polynomial clock correction (seconds)."""
    return ephemeris.af0 + ephemeris.af1 * tc_s + ephemeris.af2 * tc_s * tc_s - ephemeris.tgd


def gravity_only_periodic_eccentricity_correction_s(ephemeris: Ephemeris, eccentric_anomaly_rad: float) -> float:
    """Return the gravity-only periodic eccentricity clock term (seconds)."""
    return 0.5 * F_RELATIVISTIC * ephemeris.e * ephemeris.root_a * math.sin(eccentric_anomaly_rad)


def ballistic_orbit_longitude_rad(ephemeris: Ephemeris, tk_s: float) -> float:
    """Return orbital longitude term without Sagnac range correction.

    This is the current VSL orbit choice:
      omega_k = omega0 + (omega_dot - omega_e) * tk - omega_e * toe
    """
    return ephemeris.omega0 + (ephemeris.omega_dot - OMEGA_E_DOT_RAD_S) * tk_s - OMEGA_E_DOT_RAD_S * ephemeris.toe


def sagnac_style_orbit_longitude_rad(ephemeris: Ephemeris, tk_s: float, user_sat_range_m: float) -> float:
    """Return orbital longitude term with standard Sagnac-style range correction.

    Formula:
      omega_k = omega0 + (omega_dot - omega_e) * tk - omega_e * (toe + range / c_emit)
    """
    return (
        ephemeris.omega0
        + (ephemeris.omega_dot - OMEGA_E_DOT_RAD_S) * tk_s
        - OMEGA_E_DOT_RAD_S * (ephemeris.toe + user_sat_range_m / EMISSIONS_SPEED_OF_LIGHT_MPS)
    )
