"""VSL satellite clock correction.

The VSL model uses the broadcast polynomial clock terms (af0, af1, af2,
tgd) and does not apply an independent eccentricity-dependent clock term.
Eccentricity remains in the Keplerian orbit and therefore affects satellite
position, velocity, and ballistic propagation.

This module remains separate from the CSL clock module so the VSL clock
assumptions stay explicit and self-contained.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from src.constants import MU_M3_S2, SECONDS_IN_WEEK, SPEED_OF_LIGHT_MPS as EMISSION_SPEED_MPS
from src.models import Ephemeris
from src.vsl.corrections import polynomial_clock_correction_s

_ACCURACY_TOLERANCE = 1.0e-11
_MAX_ITERATIONS = 100


@dataclass(frozen=True)
class SatClockCorrection:
    """VSL satellite clock correction using broadcast polynomial terms."""

    satellite_clock_correction_m: float
    eccentric_anomaly_rad: float
    time_from_ref_epoch_s: float
    polynomial_correction_s: float


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
) -> SatClockCorrection:
    """Compute VSL satellite clock correction without a periodic clock term."""
    a = ephemeris.root_a * ephemeris.root_a
    n0 = math.sqrt(MU_M3_S2 / (a * a * a))
    n = n0 + ephemeris.delta_n

    tx_s = receiver_gps_week_at_transmission * SECONDS_IN_WEEK + receiver_gps_tow_at_transmission_s

    tc_s = _fix_week_rollover(tx_s - (ephemeris.week * SECONDS_IN_WEEK + ephemeris.toc))

    init_corr_s = polynomial_clock_correction_s(ephemeris, tc_s)
    sat_corr_s = init_corr_s

    counter = 0
    ecc_anom = 0.0

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

        # Strict Newtonian clock model: eccentricity affects the orbit, not
        # the clock correction. Only broadcast calibration terms are applied.
        new_corr_s = init_corr_s
        change = abs(sat_corr_s - new_corr_s)
        sat_corr_s = new_corr_s

        counter += 1
        if counter > _MAX_ITERATIONS:
            raise RuntimeError("Satellite clock correction did not converge")
        if change <= _ACCURACY_TOLERANCE:
            break

    tk_s = _fix_week_rollover(tx_s - (ephemeris.week * SECONDS_IN_WEEK + ephemeris.toe + sat_corr_s))
    return SatClockCorrection(
        satellite_clock_correction_m=sat_corr_s * EMISSION_SPEED_MPS,
        eccentric_anomaly_rad=ecc_anom,
        time_from_ref_epoch_s=tk_s,
        polynomial_correction_s=init_corr_s,
    )
