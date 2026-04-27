"""VSL correction terms.

This module isolates correction math used by the VSL clock model so the
experimental assumptions can be changed in one place.
"""

from __future__ import annotations

import math

from src.constants import (
    F_RELATIVISTIC,
    MU_M3_S2,
    OMEGA_E_DOT_RAD_S,
    SPEED_OF_LIGHT_MPS as EMISSION_SPEED_MPS,
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
        - OMEGA_E_DOT_RAD_S * (ephemeris.toe + user_sat_range_m / EMISSION_SPEED_MPS)
    )


def earth_gravitational_potential_m2ps2(radius_m: float) -> float:
    """Return Earth's Newtonian gravitational potential at radius `r`."""
    if radius_m <= 1.0:
        return 0.0
    return -MU_M3_S2 / radius_m


def gravity_adjusted_emission_speed_mps(
    sat_radius_m: float,
    rcv_radius_m: float,
) -> float:
    """Return a path-averaged gravity-adjusted emission speed.

    Experimental propagation model: deeper average potential slightly
    reduces the signal's effective propagation speed through the Earth's
    gravity well.
    """
    phi_sat = earth_gravitational_potential_m2ps2(sat_radius_m)
    phi_rcv = earth_gravitational_potential_m2ps2(rcv_radius_m)
    phi_avg = 0.5 * (phi_sat + phi_rcv)
    return EMISSION_SPEED_MPS * (1.0 + phi_avg / (EMISSION_SPEED_MPS**2))
