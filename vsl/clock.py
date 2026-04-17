"""VSL satellite clock correction.

The VSL model uses the ICD polynomial clock terms (af0, af1, af2, tgd)
but does NOT include the relativistic eccentricity correction
F * e * sqrt(A) * sin(E).

That term is a consequence of the Einsteinian clock model and is not
part of the Newtonian ballistic framework being tested here.

This module is a clean copy of the clock correction logic with the
relativistic eccentricity term unconditionally removed. It shares no
physics branching with the CSL clock module.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from src.constants import MU_M3_S2, SECONDS_IN_WEEK, SPEED_OF_LIGHT_MPS
from src.models import Ephemeris

_ACCURACY_TOLERANCE = 1.0e-11
_MAX_ITERATIONS = 100


@dataclass(frozen=True)
class SatClockCorrection:
    """VSL satellite clock correction (polynomial terms only)."""

    satellite_clock_correction_m: float
    eccentric_anomaly_rad: float
    time_from_ref_epoch_s: float


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
    """Compute VSL satellite clock correction (no relativistic eccentricity)."""
    a = ephemeris.root_a * ephemeris.root_a
    n0 = math.sqrt(MU_M3_S2 / (a * a * a))
    n = n0 + ephemeris.delta_n

    tx_s = receiver_gps_week_at_transmission * SECONDS_IN_WEEK + receiver_gps_tow_at_transmission_s

    tc_s = _fix_week_rollover(tx_s - (ephemeris.week * SECONDS_IN_WEEK + ephemeris.toc))

    init_corr_s = ephemeris.af0 + ephemeris.af1 * tc_s + ephemeris.af2 * tc_s * tc_s - ephemeris.tgd
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

        # No relativistic eccentricity term in the VSL clock model.
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
        satellite_clock_correction_m=sat_corr_s * SPEED_OF_LIGHT_MPS,
        eccentric_anomaly_rad=ecc_anom,
        time_from_ref_epoch_s=tk_s,
    )
