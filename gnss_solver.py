from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np

from gnss_parser import Ephemeris, EpochMeasurements, SatelliteObservation
from gnss_physics import (
    SPEED_OF_LIGHT_MPS,
    calculate_clock_correction,
    calculate_corrected_transmit_tow_and_week,
    calculate_satellite_position,
)


LEAST_SQUARE_TOLERANCE_METERS = 4.0e-8
MAXIMUM_NUMBER_OF_LEAST_SQUARE_ITERATIONS = 100
RESIDUAL_TO_REPEAT_LEAST_SQUARE_METERS = 20.0


@dataclass(frozen=True)
class EpochSolution:
    state_xyzb_m: np.ndarray
    residuals_m: np.ndarray
    satellite_ids: list[int]
    residual_rms_m: float


class WeightedLeastSquaresSolver:
    def __init__(self, *, enable_relativity: bool):
        self.enable_relativity = enable_relativity

    def solve_epoch(
        self,
        epoch: EpochMeasurements,
        nav_by_prn: dict[int, list[Ephemeris]],
    ) -> EpochSolution:
        observations = [obs for obs in epoch.observations if obs.svid in nav_by_prn]
        if len(observations) < 4:
            raise RuntimeError("Need at least 4 usable satellites")

        state = np.array([0.0, 0.0, 0.0, 0.0], dtype=float)

        while True:
            state, residuals, sat_ids, _ = self._run_iterative_wls(
                observations,
                epoch.receiver_tow_s,
                epoch.gps_week,
                nav_by_prn,
                state,
            )

            if len(observations) <= 4:
                break

            keep_mask = np.abs(residuals) <= RESIDUAL_TO_REPEAT_LEAST_SQUARE_METERS
            if np.all(keep_mask):
                break
            if int(np.sum(keep_mask)) < 4:
                break
            observations = [obs for obs, keep in zip(observations, keep_mask) if keep]

        residual_rms_m = math.sqrt(float(np.mean(residuals * residuals)))
        return EpochSolution(
            state_xyzb_m=state,
            residuals_m=residuals,
            satellite_ids=sat_ids,
            residual_rms_m=residual_rms_m,
        )

    def _run_iterative_wls(
        self,
        observations: list[SatelliteObservation],
        receiver_tow_s: float,
        gps_week: int,
        nav_by_prn: dict[int, list[Ephemeris]],
        initial_state: np.ndarray,
    ) -> tuple[np.ndarray, np.ndarray, list[int], list[tuple[float, float, float]]]:
        state = initial_state.copy()
        delta = np.array([np.inf, np.inf, np.inf, np.inf], dtype=float)
        iterations = 0

        residuals = np.zeros((len(observations),), dtype=float)
        sat_positions: list[tuple[float, float, float]] = []
        sat_ids: list[int] = []

        while float(np.sum(np.abs(delta[:3]))) >= LEAST_SQUARE_TOLERANCE_METERS:
            if iterations >= MAXIMUM_NUMBER_OF_LEAST_SQUARE_ITERATIONS:
                raise RuntimeError("Maximum least-square iterations reached")

            residuals, sat_positions, sat_ids = self._compute_residuals(
                observations,
                receiver_tow_s,
                gps_week,
                nav_by_prn,
                state,
            )

            h = self._geometry_matrix(sat_positions, state)
            sigmas = np.array([obs.sigma_m for obs in observations], dtype=float)
            w = np.diag(1.0 / np.maximum(sigmas * sigmas, 1e-12))

            normal = h.T @ w @ h
            rhs = h.T @ w @ residuals
            delta = np.linalg.solve(normal, rhs)

            state += delta
            iterations += 1

        residuals, sat_positions, sat_ids = self._compute_residuals(
            observations,
            receiver_tow_s,
            gps_week,
            nav_by_prn,
            state,
        )
        return state, residuals, sat_ids, sat_positions

    def _compute_residuals(
        self,
        observations: list[SatelliteObservation],
        receiver_tow_s: float,
        gps_week: int,
        nav_by_prn: dict[int, list[Ephemeris]],
        state: np.ndarray,
    ) -> tuple[np.ndarray, list[tuple[float, float, float]], list[int]]:
        residuals: list[float] = []
        sat_positions: list[tuple[float, float, float]] = []
        sat_ids: list[int] = []

        user_pos = (float(state[0]), float(state[1]), float(state[2]))
        receiver_tow_corrected_s = receiver_tow_s - state[3] / SPEED_OF_LIGHT_MPS

        for obs in observations:
            eph = self._select_ephemeris(
                nav_by_prn[obs.svid], receiver_tow_corrected_s, gps_week
            )

            tx_tow_s, tx_week = calculate_corrected_transmit_tow_and_week(
                eph,
                receiver_tow_corrected_s,
                gps_week,
                obs.pseudorange_m,
                enable_relativity=self.enable_relativity,
            )

            sat_pos = calculate_satellite_position(
                eph,
                tx_tow_s,
                tx_week,
                user_pos,
                enable_relativity=self.enable_relativity,
            )

            sat_clock_corr_m = calculate_clock_correction(
                eph,
                tx_tow_s,
                tx_week,
                enable_relativity=self.enable_relativity,
            ).satellite_clock_correction_m

            dx = sat_pos[0] - state[0]
            dy = sat_pos[1] - state[1]
            dz = sat_pos[2] - state[2]
            geometric_range_m = math.sqrt(dx * dx + dy * dy + dz * dz)
            predicted_pseudorange_m = geometric_range_m - sat_clock_corr_m + state[3]

            residuals.append(obs.pseudorange_m - predicted_pseudorange_m)
            sat_positions.append(sat_pos)
            sat_ids.append(obs.svid)

        return np.array(residuals, dtype=float), sat_positions, sat_ids

    @staticmethod
    def _geometry_matrix(
        sat_positions: list[tuple[float, float, float]],
        state: np.ndarray,
    ) -> np.ndarray:
        h = np.zeros((len(sat_positions), 4), dtype=float)
        for i, sat_pos in enumerate(sat_positions):
            dx = sat_pos[0] - state[0]
            dy = sat_pos[1] - state[1]
            dz = sat_pos[2] - state[2]
            norm = math.sqrt(dx * dx + dy * dy + dz * dz)
            h[i, 0] = (state[0] - sat_pos[0]) / norm
            h[i, 1] = (state[1] - sat_pos[1]) / norm
            h[i, 2] = (state[2] - sat_pos[2]) / norm
            h[i, 3] = 1.0
        return h

    @staticmethod
    def _select_ephemeris(
        candidates: list[Ephemeris],
        tow_s: float,
        week: int,
    ) -> Ephemeris:
        best: Ephemeris | None = None
        best_score = float("inf")
        for eph in candidates:
            dt = (week - eph.week) * 604800.0 + (tow_s - eph.toe)
            if dt > 302400.0:
                dt -= 604800.0
            elif dt < -302400.0:
                dt += 604800.0
            score = abs(dt)
            if score < best_score:
                best_score = score
                best = eph
        if best is None:
            raise RuntimeError("No ephemeris candidates")
        return best
