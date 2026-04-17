"""Reporting and CSV diagnostics — model-neutral."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import TYPE_CHECKING

from src.coordinates import distance_3d
from src.models import EpochMeasurements

if TYPE_CHECKING:
    from src.vsl.propagation import BallisticObsDebug
    from src.vsl.solver import EpochSolution as VslEpochSolution


def write_epoch_csv(
    path: Path,
    epochs: list[EpochMeasurements],
    results: dict[str, list],
    truth_ecef: tuple[float, float, float] | None,
) -> None:
    """Write per-epoch solver results to a CSV file."""
    labels = list(results.keys())
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        header = ["epoch_idx", "receiver_tow"]
        for lbl in labels:
            header += [
                f"{lbl}_solved",
                f"{lbl}_x",
                f"{lbl}_y",
                f"{lbl}_z",
                f"{lbl}_clock_bias_m",
                f"{lbl}_n_sats",
                f"{lbl}_residual_rms_m",
            ]
            if truth_ecef is not None:
                header.append(f"{lbl}_pos_error_m")
        writer.writerow(header)

        for i, epoch in enumerate(epochs):
            row: list = [i, epoch.receiver_tow_s]
            for lbl in labels:
                sol = results[lbl][i]
                if sol is None:
                    row += [0, "", "", "", "", "", ""]
                    if truth_ecef is not None:
                        row.append("")
                else:
                    pos = (float(sol.state_xyzb_m[0]), float(sol.state_xyzb_m[1]), float(sol.state_xyzb_m[2]))
                    row += [
                        1,
                        f"{pos[0]:.4f}",
                        f"{pos[1]:.4f}",
                        f"{pos[2]:.4f}",
                        f"{float(sol.state_xyzb_m[3]):.4f}",
                        len(sol.satellite_ids),
                        f"{sol.residual_rms_m:.6f}",
                    ]
                    if truth_ecef is not None:
                        row.append(f"{distance_3d(pos, truth_ecef):.4f}")
            writer.writerow(row)


def print_comparison(
    epochs: list[EpochMeasurements],
    results: dict[str, list],
    truth_ecef: tuple[float, float, float] | None,
    baseline_label: str,
) -> None:
    """Print a multi-mode comparison summary to stdout."""
    labels = list(results.keys())

    print("=" * 72)
    print("GNSS Multi-Mode Comparison")
    print("=" * 72)

    for lbl in labels:
        solutions = [s for s in results[lbl] if s is not None]
        n_solved = len(solutions)
        if n_solved == 0:
            print(f"\n  [{lbl}] No epochs solved.")
            continue

        rms_vals = sorted(s.residual_rms_m for s in solutions)
        mean_rms = sum(rms_vals) / len(rms_vals)
        median_rms = rms_vals[len(rms_vals) // 2]
        p95_rms = rms_vals[min(int(0.95 * len(rms_vals)), len(rms_vals) - 1)]
        mean_clock = sum(float(s.state_xyzb_m[3]) for s in solutions) / len(solutions)

        print(f"\n  [{lbl}]")
        print(f"    Epochs solved: {n_solved}/{len(epochs)}")
        print(f"    Residual RMS (m):  mean={mean_rms:.6f}  median={median_rms:.6f}  95th={p95_rms:.6f}")
        print(f"    Mean clock bias (m): {mean_clock:.4f}")

        if truth_ecef is not None:
            errors = []
            for s in solutions:
                pos = (float(s.state_xyzb_m[0]), float(s.state_xyzb_m[1]), float(s.state_xyzb_m[2]))
                errors.append(distance_3d(pos, truth_ecef))
            print(f"    Mean position error vs truth (m): {sum(errors) / len(errors):.4f}")

    # Pairwise comparisons against baseline
    baseline_sols = results.get(baseline_label, [])
    for lbl in labels:
        if lbl == baseline_label:
            continue
        alt_sols = results[lbl]
        pos_deltas = []
        clock_deltas = []
        rms_worse_count = 0
        both_count = 0

        for s_base, s_alt in zip(baseline_sols, alt_sols, strict=False):
            if s_base is None or s_alt is None:
                continue
            both_count += 1
            pos_b = (float(s_base.state_xyzb_m[0]), float(s_base.state_xyzb_m[1]), float(s_base.state_xyzb_m[2]))
            pos_a = (float(s_alt.state_xyzb_m[0]), float(s_alt.state_xyzb_m[1]), float(s_alt.state_xyzb_m[2]))
            pos_deltas.append(distance_3d(pos_b, pos_a))
            clock_deltas.append(float(s_alt.state_xyzb_m[3] - s_base.state_xyzb_m[3]))
            if s_alt.residual_rms_m > s_base.residual_rms_m:
                rms_worse_count += 1

        if both_count == 0:
            continue

        print(f"\n  [{lbl}] vs [{baseline_label}]  ({both_count} common epochs)")
        print(f"    Mean |delta position| (m): {sum(pos_deltas) / len(pos_deltas):.6f}")
        print(f"    Mean delta clock bias (m): {sum(clock_deltas) / len(clock_deltas):.6f}")
        print(f"    RMS worse in {rms_worse_count}/{both_count} epochs")

    print()


def write_observation_csv(
    path: Path,
    epochs: list[EpochMeasurements],
    vsl_solutions: list[VslEpochSolution | None],
    label: str = "VSL/FULL_VECTOR",
) -> None:
    """Write per-observation VSL ballistic diagnostics to a CSV file.

    One row per satellite observation in the final converged solve for each epoch.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "epoch_idx",
                "receiver_tow_s",
                "mode",
                "svid",
                "residual_m",
                "predicted_pseudorange_m",
                "flight_time_s",
                "geometric_range_equivalent_m",
                "sat_vel_magnitude_mps",
                "sat_vel_along_los_mps",
                "rcv_vel_along_los_mps",
            ]
        )

        c_mps = 299_792_458.0

        for i, (epoch, sol) in enumerate(zip(epochs, vsl_solutions, strict=False)):
            if sol is None:
                continue
            for svid, residual, debug in zip(sol.satellite_ids, sol.residuals_m, sol.obs_debug, strict=False):
                writer.writerow(
                    [
                        i,
                        f"{epoch.receiver_tow_s:.6f}",
                        label,
                        svid,
                        f"{residual:.6f}",
                        f"{debug.predicted_pseudorange_m:.4f}",
                        f"{debug.flight_time_s:.9f}",
                        f"{debug.flight_time_s * c_mps:.4f}",
                        f"{debug.sat_vel_magnitude_mps:.4f}",
                        f"{debug.sat_vel_along_los_mps:.4f}",
                        f"{debug.rcv_vel_along_los_mps:.4f}",
                    ]
                )
