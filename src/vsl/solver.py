"""VSL weighted least-squares solver."""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from src.models import Ephemeris, EpochMeasurements, SatelliteObservation
from src.vsl.config import VslConfig
from src.vsl.observation_model import compute_residuals, geometry_matrix
from src.vsl.propagation import BallisticObsDebug

_LEAST_SQUARE_TOLERANCE_M = 4.0e-8
_MAX_ITERATIONS = 100
_OUTLIER_THRESHOLD_M = 20.0
_MIN_SATS = 4


@dataclass(frozen=True)
class EpochSolution:
    """Solved receiver state for one epoch."""

    state_xyzb_m: np.ndarray
    residuals_m: np.ndarray
    satellite_ids: list[int]
    residual_rms_m: float
    obs_debug: list[BallisticObsDebug]
    correction_metrics: dict[str, float]


class WeightedLeastSquaresSolver:
    """VSL position solver using the ballistic full-vector observation model."""

    def __init__(self, config: VslConfig) -> None:
        self.config = config

    def solve_epoch(
        self,
        epoch: EpochMeasurements,
        nav_by_prn: dict[int, list[Ephemeris]],
    ) -> EpochSolution:
        """Solve one GNSS epoch with iterative WLS and outlier rejection."""
        observations = [obs for obs in epoch.observations if obs.svid in nav_by_prn]
        if len(observations) < _MIN_SATS:
            raise RuntimeError("Need at least 4 usable satellites")

        state = np.zeros(4, dtype=float)

        while True:
            state, residuals, sat_ids, _, obs_debug = self._run_iterative_wls(
                observations,
                epoch.receiver_tow_s,
                epoch.gps_week,
                nav_by_prn,
                state,
            )
            if len(observations) <= _MIN_SATS:
                break
            keep = np.abs(residuals) <= _OUTLIER_THRESHOLD_M
            if np.all(keep):
                break
            if int(np.sum(keep)) < _MIN_SATS:
                break
            observations = [o for o, k in zip(observations, keep, strict=False) if k]

        rms = math.sqrt(float(np.mean(residuals * residuals)))
        return EpochSolution(
            state_xyzb_m=state,
            residuals_m=residuals,
            satellite_ids=sat_ids,
            residual_rms_m=rms,
            obs_debug=obs_debug,
            correction_metrics=self._compute_correction_metrics(obs_debug),
        )

    @staticmethod
    def _compute_correction_metrics(obs_debug: list[BallisticObsDebug]) -> dict[str, float]:
        if not obs_debug:
            return {}
        n = len(obs_debug)
        poly = [d.sat_clock_polynomial_m for d in obs_debug]
        grav_clock = [d.sat_clock_gravity_periodic_m for d in obs_debug]
        grav_prop = [d.gravity_prop_delta_c_mps for d in obs_debug]
        return {
            "clock_poly_m": sum(poly) / n,
            "clock_poly_abs_m": sum(abs(v) for v in poly) / n,
            "clock_grav_periodic_m": sum(grav_clock) / n,
            "clock_grav_periodic_abs_m": sum(abs(v) for v in grav_clock) / n,
            "prop_gravity_delta_c_mps": sum(grav_prop) / n,
            "prop_gravity_delta_c_abs_mps": sum(abs(v) for v in grav_prop) / n,
        }

    def _run_iterative_wls(
        self,
        observations: list[SatelliteObservation],
        receiver_tow_s: float,
        gps_week: int,
        nav_by_prn: dict[int, list[Ephemeris]],
        initial_state: np.ndarray,
    ) -> tuple[np.ndarray, np.ndarray, list[int], list[tuple[float, float, float]], list[BallisticObsDebug]]:
        state = initial_state.copy()
        delta = np.full(4, np.inf)
        iterations = 0

        residuals = np.zeros(len(observations))
        sat_positions: list[tuple[float, float, float]] = []
        sat_ids: list[int] = []
        obs_debug: list[BallisticObsDebug] = []

        while float(np.sum(np.abs(delta[:3]))) >= _LEAST_SQUARE_TOLERANCE_M:
            if iterations >= _MAX_ITERATIONS:
                raise RuntimeError("Maximum least-square iterations reached")

            residuals, sat_positions, sat_ids, obs_debug = compute_residuals(
                observations,
                receiver_tow_s,
                gps_week,
                nav_by_prn,
                state,
            )

            h = geometry_matrix(sat_positions, state)
            sigmas = np.array([o.sigma_m for o in observations], dtype=float)
            w = np.diag(1.0 / np.maximum(sigmas * sigmas, 1e-12))

            delta = np.linalg.solve(h.T @ w @ h, h.T @ w @ residuals)
            state += delta
            iterations += 1

        residuals, sat_positions, sat_ids, obs_debug = compute_residuals(
            observations,
            receiver_tow_s,
            gps_week,
            nav_by_prn,
            state,
        )
        return state, residuals, sat_ids, sat_positions, obs_debug
