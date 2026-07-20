"""Ephemeris selection helper — model-neutral."""

from __future__ import annotations

from src.constants import SECONDS_IN_WEEK
from src.models import Ephemeris

_HALF_WEEK_SECONDS = SECONDS_IN_WEEK / 2.0


def select_ephemeris(
    candidates: list[Ephemeris],
    tow_s: float,
    week: int,
) -> Ephemeris:
    """Return the ephemeris whose ToE is closest to the given GPS time."""
    best: Ephemeris | None = None
    best_score = float("inf")
    for eph in candidates:
        dt = (week - eph.week) * SECONDS_IN_WEEK + (tow_s - eph.toe)
        if dt > _HALF_WEEK_SECONDS:
            dt -= SECONDS_IN_WEEK
        elif dt < -_HALF_WEEK_SECONDS:
            dt += SECONDS_IN_WEEK
        score = abs(dt)
        if score < best_score:
            best_score = score
            best = eph
    if best is None:
        raise RuntimeError("No ephemeris candidates")
    return best
