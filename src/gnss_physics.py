"""GNSS broadcast ephemeris physics helpers."""

from __future__ import annotations

import math
from dataclasses import dataclass

from src.gnss_parser import Ephemeris

SPEED_OF_LIGHT_MPS = 299792458.0
MU_M3_S2 = 3.986005e14
F_RELATIVISTIC = -4.442807633e-10
OMEGA_E_DOT_RAD_S = 7.2921151467e-5
SECONDS_IN_WEEK = 604800
ACCURACY_TOLERANCE = 1.0e-11
MAX_ITERATIONS = 100
SAT_POSITION_ITERATIONS = 5


@dataclass(frozen=True)
class SatClockCorrection:
    """Clock correction and intermediate values for one satellite."""

    satellite_clock_correction_m: float
    eccentric_anomaly_rad: float
    time_from_ref_epoch_s: float
    relativistic_correction_s: float


def fix_week_rollover(time_s: float) -> float:
    """Wrap a time delta to the GPS week interval."""
    if time_s > SECONDS_IN_WEEK / 2.0:
        return time_s - SECONDS_IN_WEEK
    if time_s < -SECONDS_IN_WEEK / 2.0:
        return time_s + SECONDS_IN_WEEK
    return time_s


def calculate_clock_correction(
    ephemeris: Ephemeris,
    receiver_gps_tow_at_transmission_s: float,
    receiver_gps_week_at_transmission: int,
    *,
    enable_relativity: bool,
) -> SatClockCorrection:
    """Compute the satellite clock correction at transmit time."""
    a = ephemeris.root_a * ephemeris.root_a
    n0 = math.sqrt(MU_M3_S2 / (a * a * a))
    n = n0 + ephemeris.delta_n

    tx_including_week_s = receiver_gps_week_at_transmission * SECONDS_IN_WEEK + receiver_gps_tow_at_transmission_s

    tc_s = tx_including_week_s - (ephemeris.week * SECONDS_IN_WEEK + ephemeris.toc)
    tc_s = fix_week_rollover(tc_s)

    init_sat_clock_correction_s = ephemeris.af0 + ephemeris.af1 * tc_s + ephemeris.af2 * tc_s * tc_s - ephemeris.tgd
    sat_clock_correction_s = init_sat_clock_correction_s

    sat_clock_corrections_counter = 0
    eccentric_anomaly_rad = 0.0

    while True:
        tk_s = tx_including_week_s - (ephemeris.week * SECONDS_IN_WEEK + ephemeris.toe + sat_clock_correction_s)
        tk_s = fix_week_rollover(tk_s)

        mean_anomaly_rad = ephemeris.m0 + n * tk_s
        eccentric_anomaly_rad = mean_anomaly_rad

        eccentric_counter = 0
        while True:
            old_e = eccentric_anomaly_rad
            eccentric_anomaly_rad = mean_anomaly_rad + ephemeris.e * math.sin(eccentric_anomaly_rad)
            eccentric_counter += 1
            if eccentric_counter > MAX_ITERATIONS:
                raise RuntimeError(f"Kepler eccentric anomaly did not converge in {MAX_ITERATIONS} iterations")
            if abs(old_e - eccentric_anomaly_rad) <= ACCURACY_TOLERANCE:
                break

        relativistic_correction_s = 0.0
        if enable_relativity:
            relativistic_correction_s = (
                F_RELATIVISTIC * ephemeris.e * ephemeris.root_a * math.sin(eccentric_anomaly_rad)
            )

        new_sat_clock_correction_s = init_sat_clock_correction_s + relativistic_correction_s
        change = abs(sat_clock_correction_s - new_sat_clock_correction_s)
        sat_clock_correction_s = new_sat_clock_correction_s

        sat_clock_corrections_counter += 1
        if sat_clock_corrections_counter > MAX_ITERATIONS:
            raise RuntimeError(f"Satellite clock correction did not converge in {MAX_ITERATIONS} iterations")

        if change <= ACCURACY_TOLERANCE:
            break

    tk_s = tx_including_week_s - (ephemeris.week * SECONDS_IN_WEEK + ephemeris.toe + sat_clock_correction_s)
    return SatClockCorrection(
        satellite_clock_correction_m=sat_clock_correction_s * SPEED_OF_LIGHT_MPS,
        eccentric_anomaly_rad=eccentric_anomaly_rad,
        time_from_ref_epoch_s=tk_s,
        relativistic_correction_s=relativistic_correction_s,
    )


def calculate_corrected_transmit_tow_and_week(
    ephemeris: Ephemeris,
    receiver_gps_tow_at_reception_s: float,
    receiver_gps_week: int,
    pseudorange_m: float,
    *,
    enable_relativity: bool,
) -> tuple[float, int]:
    """Correct a transmit TOW and GPS week for satellite clock bias."""
    receiver_gps_tow_at_tx_s = receiver_gps_tow_at_reception_s - pseudorange_m / SPEED_OF_LIGHT_MPS

    week = receiver_gps_week
    if receiver_gps_tow_at_tx_s < 0.0:
        receiver_gps_tow_at_tx_s += SECONDS_IN_WEEK
        week -= 1
    elif receiver_gps_tow_at_tx_s > SECONDS_IN_WEEK:
        receiver_gps_tow_at_tx_s -= SECONDS_IN_WEEK
        week += 1

    clock_correction_s = (
        calculate_clock_correction(
            ephemeris,
            receiver_gps_tow_at_tx_s,
            week,
            enable_relativity=enable_relativity,
        ).satellite_clock_correction_m
        / SPEED_OF_LIGHT_MPS
    )

    corrected_tow_s = receiver_gps_tow_at_tx_s + clock_correction_s
    if corrected_tow_s < 0.0:
        corrected_tow_s += SECONDS_IN_WEEK
        week -= 1
    elif corrected_tow_s > SECONDS_IN_WEEK:
        corrected_tow_s -= SECONDS_IN_WEEK
        week += 1

    return corrected_tow_s, week


def _calculate_satellite_position(
    ephemeris: Ephemeris,
    corrected_tow_s: float,
    week: int,
    user_sat_range_m: float,
    *,
    enable_relativity: bool,
) -> tuple[float, float, float]:
    sat_clock = calculate_clock_correction(
        ephemeris,
        corrected_tow_s,
        week,
        enable_relativity=enable_relativity,
    )
    e = sat_clock.eccentric_anomaly_rad
    tk_s = sat_clock.time_from_ref_epoch_s

    true_anomaly_rad = math.atan2(
        math.sqrt(1.0 - ephemeris.e * ephemeris.e) * math.sin(e),
        math.cos(e) - ephemeris.e,
    )

    argument_of_latitude_rad = true_anomaly_rad + ephemeris.omega
    radius_m = ephemeris.root_a * ephemeris.root_a * (1.0 - ephemeris.e * math.cos(e))

    radius_correction_m = ephemeris.crc * math.cos(2.0 * argument_of_latitude_rad) + ephemeris.crs * math.sin(
        2.0 * argument_of_latitude_rad
    )
    arg_lat_correction_rad = ephemeris.cuc * math.cos(2.0 * argument_of_latitude_rad) + ephemeris.cus * math.sin(
        2.0 * argument_of_latitude_rad
    )
    inclination_correction_rad = ephemeris.cic * math.cos(2.0 * argument_of_latitude_rad) + ephemeris.cis * math.sin(
        2.0 * argument_of_latitude_rad
    )

    radius_m += radius_correction_m
    argument_of_latitude_rad += arg_lat_correction_rad
    inclination_rad = ephemeris.i0 + inclination_correction_rad + ephemeris.i_dot * tk_s

    x_orb_m = radius_m * math.cos(argument_of_latitude_rad)
    y_orb_m = radius_m * math.sin(argument_of_latitude_rad)

    omega_k_rad = (
        ephemeris.omega0
        + (ephemeris.omega_dot - OMEGA_E_DOT_RAD_S) * tk_s
        - OMEGA_E_DOT_RAD_S * (ephemeris.toe + user_sat_range_m / SPEED_OF_LIGHT_MPS)
    )

    sat_x_m = x_orb_m * math.cos(omega_k_rad) - y_orb_m * math.cos(inclination_rad) * math.sin(omega_k_rad)
    sat_y_m = x_orb_m * math.sin(omega_k_rad) + y_orb_m * math.cos(inclination_rad) * math.cos(omega_k_rad)
    sat_z_m = y_orb_m * math.sin(inclination_rad)
    return sat_x_m, sat_y_m, sat_z_m


def calculate_satellite_position(
    ephemeris: Ephemeris,
    corrected_tow_s: float,
    week: int,
    user_pos_xyz_m: tuple[float, float, float],
    *,
    enable_relativity: bool,
) -> tuple[float, float, float]:
    """Compute ECEF satellite position by iterating the range estimate."""
    user_sat_range_m = 0.070 * SPEED_OF_LIGHT_MPS
    sat_x_m = sat_y_m = sat_z_m = 0.0

    for _ in range(SAT_POSITION_ITERATIONS):
        sat_x_m, sat_y_m, sat_z_m = _calculate_satellite_position(
            ephemeris,
            corrected_tow_s,
            week,
            user_sat_range_m,
            enable_relativity=enable_relativity,
        )
        dx = sat_x_m - user_pos_xyz_m[0]
        dy = sat_y_m - user_pos_xyz_m[1]
        dz = sat_z_m - user_pos_xyz_m[2]
        user_sat_range_m = math.sqrt(dx * dx + dy * dy + dz * dz)

    return sat_x_m, sat_y_m, sat_z_m
