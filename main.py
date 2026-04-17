"""Entry point for the GNSS relativity verification experiment."""

from __future__ import annotations

import math
from pathlib import Path

from src.gnss_parser import parse_gnss_logger_file, parse_rinex_nav_file
from src.gnss_physics import (
    calculate_clock_correction,
    calculate_corrected_transmit_tow_and_week,
)
from src.gnss_solver import WeightedLeastSquaresSolver

WGS84_A = 6378137.0
WGS84_E2 = 6.69437999014e-3
WEEK_SECONDS = 604800.0
HALF_WEEK_SECONDS = 302400.0
SMALL_NUMBER = 1.0e-9
SPEED_OF_LIGHT_MPS = 299792458.0


def lla_to_ecef(latitude_deg: float, longitude_deg: float, altitude_m: float) -> tuple[float, float, float]:
    """Convert geodetic coordinates to ECEF."""
    lat = math.radians(latitude_deg)
    lon = math.radians(longitude_deg)
    sin_lat = math.sin(lat)
    cos_lat = math.cos(lat)
    sin_lon = math.sin(lon)
    cos_lon = math.cos(lon)

    n = WGS84_A / math.sqrt(1.0 - WGS84_E2 * sin_lat * sin_lat)
    x = (n + altitude_m) * cos_lat * cos_lon
    y = (n + altitude_m) * cos_lat * sin_lon
    z = (n * (1.0 - WGS84_E2) + altitude_m) * sin_lat
    return x, y, z


def distance_3d(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    """Return Euclidean distance between two 3D points."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def _select_ephemeris(candidates, tow_s: float, week: int):
    best = None
    best_score = float("inf")
    for eph in candidates:
        dt = (week - eph.week) * WEEK_SECONDS + (tow_s - eph.toe)
        if dt > HALF_WEEK_SECONDS:
            dt -= WEEK_SECONDS
        elif dt < -HALF_WEEK_SECONDS:
            dt += WEEK_SECONDS
        score = abs(dt)
        if score < best_score:
            best_score = score
            best = eph
    return best


def _epoch_statistics(epochs, nav_by_prn, solver_rel, solver_no_rel, truth_ecef):  # noqa: C901
    count = 0
    residual_rms_rel = []
    residual_rms_no_rel = []
    position_delta_m = []
    clock_delta_m = []
    position_error_rel = []
    position_error_no_rel = []
    rms_increase_count = 0
    common_mode_rel_missing_m = []

    for epoch in epochs:
        try:
            sol_rel = solver_rel.solve_epoch(epoch, nav_by_prn)
            sol_no_rel = solver_no_rel.solve_epoch(epoch, nav_by_prn)
        except RuntimeError:
            continue

        count += 1
        residual_rms_rel.append(sol_rel.residual_rms_m)
        residual_rms_no_rel.append(sol_no_rel.residual_rms_m)

        pos_rel = (
            float(sol_rel.state_xyzb_m[0]),
            float(sol_rel.state_xyzb_m[1]),
            float(sol_rel.state_xyzb_m[2]),
        )
        pos_no_rel = (
            float(sol_no_rel.state_xyzb_m[0]),
            float(sol_no_rel.state_xyzb_m[1]),
            float(sol_no_rel.state_xyzb_m[2]),
        )
        position_delta_m.append(distance_3d(pos_rel, pos_no_rel))
        clock_delta_m.append(float(sol_no_rel.state_xyzb_m[3] - sol_rel.state_xyzb_m[3]))

        if sol_no_rel.residual_rms_m > sol_rel.residual_rms_m:
            rms_increase_count += 1

        if truth_ecef is not None:
            position_error_rel.append(distance_3d(pos_rel, truth_ecef))
            position_error_no_rel.append(distance_3d(pos_no_rel, truth_ecef))

        rel_terms = []
        receiver_tow_corrected = epoch.receiver_tow_s - sol_no_rel.state_xyzb_m[3] / SPEED_OF_LIGHT_MPS
        for obs in epoch.observations:
            if obs.svid not in nav_by_prn:
                continue
            eph = _select_ephemeris(nav_by_prn[obs.svid], receiver_tow_corrected, epoch.gps_week)
            if eph is None:
                continue
            tx_tow, tx_week = calculate_corrected_transmit_tow_and_week(
                eph,
                receiver_tow_corrected,
                epoch.gps_week,
                obs.pseudorange_m,
                enable_relativity=False,
            )
            with_rel = calculate_clock_correction(
                eph,
                tx_tow,
                tx_week,
                enable_relativity=True,
            ).satellite_clock_correction_m
            without_rel = calculate_clock_correction(
                eph,
                tx_tow,
                tx_week,
                enable_relativity=False,
            ).satellite_clock_correction_m
            rel_terms.append(with_rel - without_rel)
        if rel_terms:
            common_mode_rel_missing_m.append(sum(rel_terms) / len(rel_terms))

    return {
        "count": count,
        "residual_rms_rel": residual_rms_rel,
        "residual_rms_no_rel": residual_rms_no_rel,
        "position_delta_m": position_delta_m,
        "clock_delta_m": clock_delta_m,
        "position_error_rel": position_error_rel,
        "position_error_no_rel": position_error_no_rel,
        "rms_increase_count": rms_increase_count,
        "common_mode_rel_missing_m": common_mode_rel_missing_m,
    }


def _print_summary(stats, epochs_len):  # noqa: PLR0915
    count = stats["count"]
    if count == 0:
        raise RuntimeError("No epochs solved successfully")

    residual_rms_rel = stats["residual_rms_rel"]
    residual_rms_no_rel = stats["residual_rms_no_rel"]
    position_delta_m = stats["position_delta_m"]
    clock_delta_m = stats["clock_delta_m"]
    position_error_rel = stats["position_error_rel"]
    position_error_no_rel = stats["position_error_no_rel"]

    mean_rms_rel = sum(residual_rms_rel) / len(residual_rms_rel)
    mean_rms_no_rel = sum(residual_rms_no_rel) / len(residual_rms_no_rel)
    mean_pos_delta = sum(position_delta_m) / len(position_delta_m)
    mean_clock_delta = sum(clock_delta_m) / len(clock_delta_m)

    print("GNSS Relativity Verification")
    print(f"Epochs solved: {count}/{epochs_len}")
    print()
    print("Residual RMS (meters):")
    print(f"  relativity ON : {mean_rms_rel:.6f}")
    print(f"  relativity OFF: {mean_rms_no_rel:.6f}")
    print(f"  delta OFF-ON  : {mean_rms_no_rel - mean_rms_rel:.6f}")
    print(f"  OFF > ON in   : {stats['rms_increase_count']}/{count} epochs")
    print()
    print("Position / Clock impact:")
    print(f"  mean |delta position| (m): {mean_pos_delta:.6f}")
    print(f"  mean delta clock bias (m): {mean_clock_delta:.6f}")

    if stats["common_mode_rel_missing_m"]:
        common_mode = sum(stats["common_mode_rel_missing_m"]) / len(stats["common_mode_rel_missing_m"])
        absorbed_fraction = (
            abs(mean_clock_delta) / abs(common_mode) if abs(common_mode) > SMALL_NUMBER else float("nan")
        )
        print(f"  mean missing-relativity common mode (m): {common_mode:.6f}")
        print(f"  clock absorption ratio (|dClock|/|common|): {absorbed_fraction:.6f}")

    if position_error_rel and position_error_no_rel:
        mean_err_rel = sum(position_error_rel) / len(position_error_rel)
        mean_err_no_rel = sum(position_error_no_rel) / len(position_error_no_rel)
        print()
        print("Position error vs first Fix ECEF (meters):")
        print(f"  relativity ON : {mean_err_rel:.6f}")
        print(f"  relativity OFF: {mean_err_no_rel:.6f}")
        print(f"  delta OFF-ON  : {mean_err_no_rel - mean_err_rel:.6f}")

    disproved = mean_rms_no_rel > mean_rms_rel
    print()
    print(
        "Conclusion: disabling relativity "
        + ("increases" if disproved else "does not increase")
        + " residual RMS on average."
    )


def main() -> None:
    """Run the relativity comparison experiment and print a summary."""
    root = Path(__file__).resolve().parent
    log_path = root / "data" / "pseudoranges_log_2016_06_30_21_26_07.txt"
    rinex_path = root / "data" / "hour1820.16n"

    gps_week = 1903
    epochs, fixes = parse_gnss_logger_file(log_path, gps_week=gps_week)
    nav_by_prn = parse_rinex_nav_file(rinex_path)

    if not epochs:
        raise RuntimeError("No usable epochs parsed from GNSS log")

    truth_ecef = None
    if fixes:
        truth_ecef = lla_to_ecef(
            fixes[0].latitude_deg,
            fixes[0].longitude_deg,
            fixes[0].altitude_m,
        )

    solver_rel = WeightedLeastSquaresSolver(enable_relativity=True)
    solver_no_rel = WeightedLeastSquaresSolver(enable_relativity=False)
    stats = _epoch_statistics(epochs, nav_by_prn, solver_rel, solver_no_rel, truth_ecef)
    _print_summary(stats, len(epochs))


if __name__ == "__main__":
    main()
