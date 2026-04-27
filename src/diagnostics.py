# ruff: noqa: C901, PLR0915
"""Reporting and CSV diagnostics — model-neutral."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import TYPE_CHECKING

from src.coordinates import distance_3d
from src.models import EpochMeasurements

if TYPE_CHECKING:
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

    with path.open("w", newline="") as f:
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
    summaries: dict[str, dict[str, float | int | None]] = {}

    print("=" * 72)
    print("GNSS Multi-Mode Comparison")
    print("=" * 72)

    for lbl in labels:
        solutions = [s for s in results[lbl] if s is not None]
        n_solved = len(solutions)
        summary: dict[str, float | int | None] = {
            "solved": n_solved,
            "mean_rms": None,
            "delta_rms": 0.0 if lbl == baseline_label else None,
            "worse_epochs": None if lbl != baseline_label else 0,
            "mean_pos_diff": 0.0 if lbl == baseline_label else None,
            "pos_err": None,
        }
        if n_solved > 0:
            summary["mean_rms"] = sum(s.residual_rms_m for s in solutions) / len(solutions)
            if truth_ecef is not None:
                errors = []
                for s in solutions:
                    pos = (float(s.state_xyzb_m[0]), float(s.state_xyzb_m[1]), float(s.state_xyzb_m[2]))
                    errors.append(distance_3d(pos, truth_ecef))
                summary["pos_err"] = sum(errors) / len(errors)
        summaries[lbl] = summary

    baseline_sols = results.get(baseline_label, [])
    for lbl in labels:
        if lbl == baseline_label:
            continue
        alt_sols = results[lbl]
        pos_deltas = []
        rms_deltas = []
        rms_worse_count = 0
        both_count = 0

        for s_base, s_alt in zip(baseline_sols, alt_sols, strict=False):
            if s_base is None or s_alt is None:
                continue
            both_count += 1
            pos_b = (float(s_base.state_xyzb_m[0]), float(s_base.state_xyzb_m[1]), float(s_base.state_xyzb_m[2]))
            pos_a = (float(s_alt.state_xyzb_m[0]), float(s_alt.state_xyzb_m[1]), float(s_alt.state_xyzb_m[2]))
            pos_deltas.append(distance_3d(pos_b, pos_a))
            rms_deltas.append(s_alt.residual_rms_m - s_base.residual_rms_m)
            if s_alt.residual_rms_m > s_base.residual_rms_m:
                rms_worse_count += 1

        if both_count == 0:
            continue

        summaries[lbl]["delta_rms"] = sum(rms_deltas) / len(rms_deltas)
        summaries[lbl]["worse_epochs"] = rms_worse_count
        summaries[lbl]["mean_pos_diff"] = sum(pos_deltas) / len(pos_deltas)

    model_width = max(len("Model"), max(len(lbl) for lbl in labels))
    solved_width = max(len("Solved"), len(f"{len(epochs)}/{len(epochs)}"))
    mean_rms_width = len("Mean RMS")
    delta_rms_width = len("Mean RMS Change vs CSL")
    worse_width = len("Worse Epochs")
    pos_diff_width = len("Mean 3D Position Difference vs CSL")
    pos_err_width = len("Pos Err vs Fix")
    table_width = (
        model_width
        + solved_width
        + mean_rms_width
        + delta_rms_width
        + worse_width
        + pos_diff_width
        + pos_err_width
        + 18
    )

    print("Model Summary")
    print("-" * table_width)
    print(
        f"{'Model':<{model_width}} | "
        f"{'Solved':>{solved_width}} | "
        f"{'Mean RMS':>{mean_rms_width}} | "
        f"{'Mean RMS Change vs CSL':>{delta_rms_width}} | "
        f"{'Worse Epochs':>{worse_width}} | "
        f"{'Mean 3D Position Difference vs CSL':>{pos_diff_width}} | "
        f"{'Pos Err vs Fix':>{pos_err_width}}"
    )
    print("-" * table_width)
    for lbl in labels:
        summary = summaries[lbl]
        solved = f"{int(summary['solved'])}/{len(epochs)}"
        mean_rms = "--" if summary["mean_rms"] is None else f"{float(summary['mean_rms']):.3f}"
        if lbl == baseline_label:
            delta_rms = "baseline"
            worse = "baseline"
            pos_diff = "baseline"
        else:
            delta_rms = "--" if summary["delta_rms"] is None else f"{float(summary['delta_rms']):+.3f}"
            worse = (
                "--" if summary["worse_epochs"] is None else f"{int(summary['worse_epochs'])}/{int(summary['solved'])}"
            )
            pos_diff = "--" if summary["mean_pos_diff"] is None else f"{float(summary['mean_pos_diff']):.3f}"
        pos_err = "--" if summary["pos_err"] is None else f"{float(summary['pos_err']):.3f}"
        print(
            f"{lbl:<{model_width}} | "
            f"{solved:>{solved_width}} | "
            f"{mean_rms:>{mean_rms_width}} | "
            f"{delta_rms:>{delta_rms_width}} | "
            f"{worse:>{worse_width}} | "
            f"{pos_diff:>{pos_diff_width}} | "
            f"{pos_err:>{pos_err_width}}"
        )

    ranked = [
        (lbl, float(summary["mean_rms"])) for lbl, summary in summaries.items() if summary["mean_rms"] is not None
    ]
    ranked.sort(key=lambda item: item[1])

    print("\nInterpretation")
    if ranked:
        print(f"- Best fit to measurements: {ranked[0][0]}")
    for lbl in labels:
        if lbl == baseline_label:
            continue
        summary = summaries[lbl]
        if summary["delta_rms"] is None or summary["worse_epochs"] is None:
            continue
        print(
            f"- {lbl}: mean RMS change vs {baseline_label} = {float(summary['delta_rms']):+.3f} m; "
            f"worse in {int(summary['worse_epochs'])}/{int(summary['solved'])} epochs."
        )

    print("\nNotes")
    print("  - Relative comparisons against CSL are the strongest signal in this experiment.")
    if truth_ecef is not None:
        print("  - 'Pos Err vs Fix' uses the phone logger Fix as a coarse external reference, not survey truth.")
    if summaries.get(baseline_label, {}).get("mean_rms") is not None:
        print(
            "  - Large absolute residual RMS can be dominated by measurement-model limitations "
            "(timing heuristics, atmosphere, multipath), even when model deltas are meaningful."
        )

    print("\nAverage Corrections")
    correction_rows = [
        ("clock_poly_m", "clock_poly_abs_m", "Clock Polynomial", "m"),
        ("clock_rel_ecc_m", "clock_rel_ecc_abs_m", "Clock Rel Eccentricity", "m"),
        ("clock_grav_periodic_m", "clock_grav_periodic_abs_m", "Clock Gravity Periodic", "m"),
        ("sagnac_equiv_m", "sagnac_equiv_abs_m", "Sagnac Equivalent", "m"),
        ("prop_gravity_delta_c_mps", "prop_gravity_delta_c_abs_mps", "Propagation Gravity dC", "m/s"),
    ]
    for lbl in labels:
        solutions = [s for s in results[lbl] if s is not None]
        if not solutions:
            continue
        metric_values: dict[str, list[float]] = {}
        for sol in solutions:
            metrics = getattr(sol, "correction_metrics", {})
            for key, value in metrics.items():
                metric_values.setdefault(key, []).append(float(value))

        if not metric_values:
            continue

        mean_metrics = {key: (sum(values) / len(values)) for key, values in metric_values.items()}

        rows: list[tuple[str, str, str, str]] = []
        for signed_key, abs_key, name, unit in correction_rows:
            if signed_key not in mean_metrics and abs_key not in mean_metrics:
                continue
            signed = "--" if signed_key not in mean_metrics else f"{mean_metrics[signed_key]:+.6f}"
            abs_value = "--" if abs_key not in mean_metrics else f"{mean_metrics[abs_key]:+.6f}"
            rows.append((name, signed, abs_value, unit))

        if not rows:
            continue

        metric_width = max(len("Correction"), max(len(row[0]) for row in rows))
        mean_width = max(len("Mean"), max(len(row[1]) for row in rows))
        abs_width = max(len("Mean Abs"), max(len(row[2]) for row in rows))
        unit_width = max(len("Unit"), max(len(row[3]) for row in rows))
        table_width = metric_width + mean_width + abs_width + unit_width + 9

        print(f"- {lbl}")
        print("  " + "-" * table_width)
        print(
            f"  {'Correction':<{metric_width}} | {'Mean':>{mean_width}} | "
            f"{'Mean Abs':>{abs_width}} | {'Unit':<{unit_width}}"
        )
        print("  " + "-" * table_width)
        for name, signed, abs_value, unit in rows:
            print(
                f"  {name:<{metric_width}} | {signed:>{mean_width}} | {abs_value:>{abs_width}} | {unit:<{unit_width}}"
            )

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

    with path.open("w", newline="") as f:
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
