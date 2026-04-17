"""VSL satellite orbit computation.

Computes satellite ECEF position and velocity from broadcast Keplerian
elements. Velocity is needed by the ballistic propagation model to
inherit the source velocity vector.

The standard ICD orbit equations are used for position. The Sagnac /
Earth-rotation longitude correction (user_sat_range / c term) is NOT
applied here because the ballistic propagation model handles Earth
rotation explicitly through moving-receiver interception. Applying both
would double-count the Earth-rotation effect.

This module belongs entirely to the VSL package.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from src.constants import MU_M3_S2, OMEGA_E_DOT_RAD_S, SECONDS_IN_WEEK, SPEED_OF_LIGHT_MPS
from src.models import Ephemeris

from vsl.clock import SatClockCorrection, calculate_clock_correction

_SAT_POSITION_ITERATIONS = 5


@dataclass(frozen=True)
class SatelliteState:
    """Satellite ECEF position and velocity at a point in time."""

    pos_m: tuple[float, float, float]
    vel_mps: tuple[float, float, float]


def _satellite_position_no_sagnac(
    ephemeris: Ephemeris,
    sat_clock: SatClockCorrection,
) -> tuple[float, float, float]:
    """Compute ECEF satellite position without the Sagnac range correction.

    The ballistic model handles Earth rotation through receiver motion;
    adding the standard user_sat_range/c term on top would double-count it.
    """
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

    # Longitude of ascending node — no user_sat_range/c Sagnac term
    omega_k = ephemeris.omega0 + (ephemeris.omega_dot - OMEGA_E_DOT_RAD_S) * tk_s - OMEGA_E_DOT_RAD_S * ephemeris.toe

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
) -> tuple[float, float, float]:
    """Compute ECEF satellite position (no Sagnac) for geometry matrix use."""
    # Iterate to get a stable position (without the Sagnac range adjustment)
    sx = sy = sz = 0.0
    for _ in range(_SAT_POSITION_ITERATIONS):
        sat_clock = calculate_clock_correction(ephemeris, corrected_tow_s, week)
        sx, sy, sz = _satellite_position_no_sagnac(ephemeris, sat_clock)
        # Range is computed but not fed back into the omega_k formula
        dx = sx - user_pos_xyz_m[0]
        dy = sy - user_pos_xyz_m[1]
        dz = sz - user_pos_xyz_m[2]
        _ = math.sqrt(dx * dx + dy * dy + dz * dz)  # kept for future use if needed
    return sx, sy, sz


def calculate_satellite_state(
    ephemeris: Ephemeris,
    corrected_tow_s: float,
    week: int,
) -> SatelliteState:
    """Compute satellite ECEF position and velocity analytically.

    Velocity is computed by differentiating the broadcast Keplerian orbit
    model. The result includes the ECEF frame-rotation contribution.
    No Sagnac range correction is applied (see module docstring).
    """
    sat_clock = calculate_clock_correction(ephemeris, corrected_tow_s, week)
    e = sat_clock.eccentric_anomaly_rad
    tk_s = sat_clock.time_from_ref_epoch_s

    a = ephemeris.root_a * ephemeris.root_a
    n0 = math.sqrt(MU_M3_S2 / (a * a * a))
    n = n0 + ephemeris.delta_n
    ecc = ephemeris.e

    sin_e = math.sin(e)
    cos_e = math.cos(e)
    e_dot = n / (1.0 - ecc * cos_e)

    sqrt_1me2 = math.sqrt(1.0 - ecc * ecc)
    true_anom = math.atan2(sqrt_1me2 * sin_e, cos_e - ecc)
    true_anom_dot = e_dot * sqrt_1me2 / (1.0 - ecc * cos_e)

    u = true_anom + ephemeris.omega
    sin_2u = math.sin(2.0 * u)
    cos_2u = math.cos(2.0 * u)

    du = ephemeris.cuc * cos_2u + ephemeris.cus * sin_2u
    dr = ephemeris.crc * cos_2u + ephemeris.crs * sin_2u
    di = ephemeris.cic * cos_2u + ephemeris.cis * sin_2u

    u_corr = u + du
    r = a * (1.0 - ecc * cos_e) + dr
    inc = ephemeris.i0 + di + ephemeris.i_dot * tk_s

    u_dot = true_anom_dot * (1.0 + 2.0 * (-ephemeris.cuc * sin_2u + ephemeris.cus * cos_2u))
    r_dot = a * ecc * sin_e * e_dot + 2.0 * true_anom_dot * (-ephemeris.crc * sin_2u + ephemeris.crs * cos_2u)
    inc_dot = ephemeris.i_dot + 2.0 * true_anom_dot * (-ephemeris.cic * sin_2u + ephemeris.cis * cos_2u)

    x_orb = r * math.cos(u_corr)
    y_orb = r * math.sin(u_corr)
    x_orb_dot = r_dot * math.cos(u_corr) - r * u_dot * math.sin(u_corr)
    y_orb_dot = r_dot * math.sin(u_corr) + r * u_dot * math.cos(u_corr)

    omega_k = ephemeris.omega0 + (ephemeris.omega_dot - OMEGA_E_DOT_RAD_S) * tk_s - OMEGA_E_DOT_RAD_S * ephemeris.toe
    omega_k_dot = ephemeris.omega_dot - OMEGA_E_DOT_RAD_S

    sin_ok = math.sin(omega_k)
    cos_ok = math.cos(omega_k)
    sin_i = math.sin(inc)
    cos_i = math.cos(inc)

    sx = x_orb * cos_ok - y_orb * cos_i * sin_ok
    sy = x_orb * sin_ok + y_orb * cos_i * cos_ok
    sz = y_orb * sin_i

    vx = (
        x_orb_dot * cos_ok
        - y_orb_dot * cos_i * sin_ok
        - omega_k_dot * (x_orb * sin_ok + y_orb * cos_i * cos_ok)
        + y_orb * inc_dot * sin_i * sin_ok
    )
    vy = (
        x_orb_dot * sin_ok
        + y_orb_dot * cos_i * cos_ok
        + omega_k_dot * (x_orb * cos_ok - y_orb * cos_i * sin_ok)
        - y_orb * inc_dot * sin_i * cos_ok
    )
    vz = y_orb_dot * sin_i + y_orb * inc_dot * cos_i

    return SatelliteState(pos_m=(sx, sy, sz), vel_mps=(vx, vy, vz))
