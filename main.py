"""Experiment orchestrator: multi-mode GNSS comparison.

Runs the CSL (constant-speed-light) and VSL (ballistic full-vector)
solvers side by side on the same dataset and reports comparison metrics.

Usage:
  uv run python main.py                  # runs both bundled datasets
  uv run python main.py --dataset 1      # first dataset only (June 2016)
  uv run python main.py --dataset 2      # second dataset only (August 2016)
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from src.coordinates import lla_to_ecef
from src.csl.config import NO_RELATIVITY_CONFIG, STANDARD_CONFIG
from src.csl.solver import EpochSolution as CslSolution, WeightedLeastSquaresSolver as CslSolver
from src.diagnostics import print_comparison, write_epoch_csv, write_observation_csv
from src.measurement_parser import parse_gnss_logger_file
from src.models import Ephemeris, EpochMeasurements
from src.nav_parser import parse_rinex_nav_file
from src.vsl.config import BALLISTIC_FULL_VECTOR_CONFIG
from src.vsl.solver import EpochSolution as VslSolution, WeightedLeastSquaresSolver as VslSolver


@dataclass(frozen=True)
class DatasetConfig:
    """Paths and GPS week for one measurement dataset."""

    name: str
    log_path: Path
    rinex_path: Path
    gps_week: int


def _datasets(root: Path) -> list[DatasetConfig]:
    return [
        DatasetConfig(
            name="dataset1_2016-06-30",
            log_path=root / "data" / "pseudoranges_log_2016_06_30_21_26_07.txt",
            rinex_path=root / "data" / "hour1820.16n",
            gps_week=1903,
        ),
        DatasetConfig(
            name="dataset2_2016-08-22",
            log_path=root / "data" / "pseudoranges_log_2016_08_22_14_45_50.txt",
            rinex_path=root / "data" / "hour2350.16n",
            gps_week=1910,
        ),
    ]


def _solve_all(
    epochs: list[EpochMeasurements],
    nav_by_prn: dict[int, list[Ephemeris]],
) -> dict[str, list[CslSolution | VslSolution | None]]:
    """Run all model configurations over all epochs."""
    solvers: dict[str, CslSolver | VslSolver] = {
        STANDARD_CONFIG.label: CslSolver(STANDARD_CONFIG),
        NO_RELATIVITY_CONFIG.label: CslSolver(NO_RELATIVITY_CONFIG),
        BALLISTIC_FULL_VECTOR_CONFIG.label: VslSolver(BALLISTIC_FULL_VECTOR_CONFIG),
    }

    results: dict[str, list] = {label: [] for label in solvers}

    for epoch in epochs:
        for label, solver in solvers.items():
            try:
                sol = solver.solve_epoch(epoch, nav_by_prn)
            except RuntimeError:
                sol = None
            results[label].append(sol)

    return results


def _run_dataset(ds: DatasetConfig, output_dir: Path) -> None:
    print(f"\n{'=' * 72}")
    print(f"Dataset: {ds.name}")
    print(f"  Log:   {ds.log_path.name}")
    print(f"  RINEX: {ds.rinex_path.name}  (GPS week {ds.gps_week})")

    epochs, fixes = parse_gnss_logger_file(ds.log_path, gps_week=ds.gps_week)
    nav_by_prn = parse_rinex_nav_file(ds.rinex_path)

    if not epochs:
        print("  WARNING: No usable epochs parsed — skipping dataset.")
        return

    truth_ecef = None
    if fixes:
        truth_ecef = lla_to_ecef(
            fixes[0].latitude_deg,
            fixes[0].longitude_deg,
            fixes[0].altitude_m,
        )

    results = _solve_all(epochs, nav_by_prn)

    print_comparison(epochs, results, truth_ecef, baseline_label=STANDARD_CONFIG.label)

    epoch_csv = output_dir / f"{ds.name}_epoch_diagnostics.csv"
    write_epoch_csv(epoch_csv, epochs, results, truth_ecef)
    print(f"  Epoch diagnostics: {epoch_csv}")

    vsl_label = BALLISTIC_FULL_VECTOR_CONFIG.label
    vsl_solutions = results[vsl_label]
    obs_csv = output_dir / f"{ds.name}_observation_diagnostics.csv"
    write_observation_csv(obs_csv, epochs, vsl_solutions, label=vsl_label)
    print(f"  Observation diagnostics: {obs_csv}")


def main() -> None:
    """Load data, run all models, print comparison, write diagnostics CSVs."""
    parser = argparse.ArgumentParser(description="GNSS multi-mode experiment")
    parser.add_argument(
        "--dataset",
        type=int,
        choices=[1, 2],
        default=None,
        help="Run only dataset 1 (June 2016) or dataset 2 (August 2016). Default: both.",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    output_dir = root / "output"
    all_datasets = _datasets(root)

    datasets_to_run = [all_datasets[args.dataset - 1]] if args.dataset is not None else all_datasets

    for ds in datasets_to_run:
        _run_dataset(ds, output_dir)


if __name__ == "__main__":
    main()
