"""CSL satellite clock correction (ICD-GPS-200 broadcast model).

This module owns all satellite clock correction logic for the constant-
speed-light model, including the optional relativistic eccentricity term
F * e * sqrt(A) * sin(E).

Nothing in this module belongs to the VSL / ballistic package.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from src.constants import MU_M3_S2, SECONDS_IN_WEEK, SPEED_OF_LIGHT_MPS
from src.csl.config import CslConfig
from src.csl.corrections import polynomial_clock_correction_s, relativistic_eccentricity_correction_s
from src.models import Ephemeris

_ACCURACY_TOLERANCE = 1.0e-11
_MAX_ITERATIONS = 100


@dataclass(frozen=True)
class SatClockCorrection:
    """Clock correction and intermediate values for one satellite."""

    satellite_clock_correction_m: float
    eccentric_anomaly_rad: float
    time_from_ref_epoch_s: float
    relativistic_correction_s: float


def _fix_week_rollover(time_s: float) -> float:
    half = SECONDS_IN_WEEK / 2.0
    if time_s > half:
        return time_s - SECONDS_IN_WEEK
    if time_s < -half:
        return time_s + SECONDS_IN_WEEK
    return time_s


def calculate_clock_correction(
    ephemeris: Ephemeris,
    receiver_gps_tow_at_transmission_s: float,
    receiver_gps_week_at_transmission: int,
    config: CslConfig,
) -> SatClockCorrection:
    """Compute satellite clock correction at transmit time (ICD-GPS-200)."""
    a = ephemeris.root_a * ephemeris.root_a
    n0 = math.sqrt(MU_M3_S2 / (a * a * a))
    n = n0 + ephemeris.delta_n

    tx_s = receiver_gps_week_at_transmission * SECONDS_IN_WEEK + receiver_gps_tow_at_transmission_s

    tc_s = _fix_week_rollover(tx_s - (ephemeris.week * SECONDS_IN_WEEK + ephemeris.toc))

    init_corr_s = polynomial_clock_correction_s(ephemeris, tc_s)
    sat_corr_s = init_corr_s

    counter = 0
    eccentric_anomaly_rad = 0.0

    while True:
        tk_s = _fix_week_rollover(tx_s - (ephemeris.week * SECONDS_IN_WEEK + ephemeris.toe + sat_corr_s))

        mean_anom = ephemeris.m0 + n * tk_s
        ecc_anom = mean_anom
        ecc_counter = 0
        while True:
            old = ecc_anom
            ecc_anom = mean_anom + ephemeris.e * math.sin(ecc_anom)
            ecc_counter += 1
            if ecc_counter > _MAX_ITERATIONS:
                raise RuntimeError("Kepler eccentric anomaly did not converge")
            if abs(old - ecc_anom) <= _ACCURACY_TOLERANCE:
                break
        eccentric_anomaly_rad = ecc_anom

        rel_corr_s = 0.0
        if config.enable_relativistic_eccentricity:
            rel_corr_s = relativistic_eccentricity_correction_s(ephemeris, ecc_anom)

        new_corr_s = init_corr_s + rel_corr_s
        change = abs(sat_corr_s - new_corr_s)
        sat_corr_s = new_corr_s

        counter += 1
        if counter > _MAX_ITERATIONS:
            raise RuntimeError("Satellite clock correction did not converge")
        if change <= _ACCURACY_TOLERANCE:
            break

    tk_s = _fix_week_rollover(tx_s - (ephemeris.week * SECONDS_IN_WEEK + ephemeris.toe + sat_corr_s))
    return SatClockCorrection(
        satellite_clock_correction_m=sat_corr_s * SPEED_OF_LIGHT_MPS,
        eccentric_anomaly_rad=eccentric_anomaly_rad,
        time_from_ref_epoch_s=tk_s,
        relativistic_correction_s=rel_corr_s if config.enable_relativistic_eccentricity else 0.0,
    )


def calculate_corrected_transmit_tow_and_week(
    ephemeris: Ephemeris,
    receiver_gps_tow_at_reception_s: float,
    receiver_gps_week: int,
    pseudorange_m: float,
    config: CslConfig,
) -> tuple[float, int]:
    """Return corrected transmit TOW and GPS week given a pseudorange."""
    tow_tx = receiver_gps_tow_at_reception_s - pseudorange_m / SPEED_OF_LIGHT_MPS
    week = receiver_gps_week

    if tow_tx < 0.0:
        tow_tx += SECONDS_IN_WEEK
        week -= 1
    elif tow_tx > SECONDS_IN_WEEK:
        tow_tx -= SECONDS_IN_WEEK
        week += 1

    corr_s = (
        calculate_clock_correction(ephemeris, tow_tx, week, config).satellite_clock_correction_m / SPEED_OF_LIGHT_MPS
    )

    corrected_tow = tow_tx + corr_s
    if corrected_tow < 0.0:
        corrected_tow += SECONDS_IN_WEEK
        week -= 1
    elif corrected_tow > SECONDS_IN_WEEK:
        corrected_tow -= SECONDS_IN_WEEK
        week += 1

    return corrected_tow, week
