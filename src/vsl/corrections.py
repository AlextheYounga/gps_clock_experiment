"""VSL correction terms.

This module isolates correction math used by the VSL model so the
experimental assumptions can be changed in one place.
"""

from __future__ import annotations

import math

from src.constants import (
    MU_M3_S2,
    OMEGA_E_DOT_RAD_S,
    SPEED_OF_LIGHT_MPS as EMISSION_SPEED_MPS,
)
from src.models import Ephemeris


def polynomial_clock_correction_s(ephemeris: Ephemeris, tc_s: float) -> float:
    """Return broadcast polynomial clock correction (seconds)."""
    return ephemeris.af0 + ephemeris.af1 * tc_s + ephemeris.af2 * tc_s * tc_s - ephemeris.tgd


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


def earth_rotation_velocity_mps(position_m: tuple[float, float, float]) -> tuple[float, float, float]:
    """Return the ECEF-frame velocity induced by Earth rotation at a position."""
    x_m, y_m, _ = position_m
    return -OMEGA_E_DOT_RAD_S * y_m, OMEGA_E_DOT_RAD_S * x_m, 0.0


def ecef_to_inertial_velocity_mps(
    position_m: tuple[float, float, float],
    ecef_velocity_mps: tuple[float, float, float],
) -> tuple[float, float, float]:
    """Return inertial velocity expressed in the transmit-time ECEF basis.

    The ballistic propagation solve rotates the receiver from reception into
    the transmit-time-oriented basis. Satellite velocity must be expressed in
    that same basis, so its Earth-frame rotation component is restored.
    """
    rotation_velocity_mps = earth_rotation_velocity_mps(position_m)
    return tuple(ecef_velocity_mps[index] + rotation_velocity_mps[index] for index in range(3))


def rotate_ecef_position_forward(
    position_m: tuple[float, float, float],
    duration_s: float,
) -> tuple[float, float, float]:
    """Rotate an ECEF position forward into the transmit-time inertial basis."""
    angle = OMEGA_E_DOT_RAD_S * duration_s
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    x_m, y_m, z_m = position_m
    return (
        x_m * cos_angle - y_m * sin_angle,
        x_m * sin_angle + y_m * cos_angle,
        z_m,
    )


def earth_gravitational_potential_m2ps2(radius_m: float) -> float:
    """Return Earth's Newtonian gravitational potential at radius `r`."""
    if radius_m <= 1.0:
        return 0.0
    return -MU_M3_S2 / radius_m


def effective_light_speed_mps(satellite_radius_m: float, receiver_radius_m: float) -> float:
    """Return the path-averaged light speed from Newtonian energy conservation.

    Treats the emitted signal as a Newtonian corpuscle fired at
    EMISSION_SPEED_MPS from the satellite radius and moving through
    Earth's gravitational field to the receiver radius. Conservation of
    mechanical energy gives the speed at the receiver:

        v_received = sqrt(c_emit^2 + 2 * (phi_satellite - phi_receiver))

    Falling light speeds up; rising light slows down. The flight-time
    solver uses the average of the emitted and received speeds.
    """
    phi_satellite = earth_gravitational_potential_m2ps2(satellite_radius_m)
    phi_receiver = earth_gravitational_potential_m2ps2(receiver_radius_m)
    received_light_speed_mps = math.sqrt(
        EMISSION_SPEED_MPS**2 + 2.0 * (phi_satellite - phi_receiver)
    )
    return 0.5 * (EMISSION_SPEED_MPS + received_light_speed_mps)
