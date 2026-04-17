"""GNSS Logger measurement file parser."""

from __future__ import annotations

from pathlib import Path

from src.constants import SPEED_OF_LIGHT_MPS
from src.models import EpochMeasurements, FixRecord, SatelliteObservation

_SECONDS_PER_NANO = 1e-9
_GPS_CHIP_WIDTH_T_C_SEC = 1.0e-6
_GPS_CORRELATOR_SPACING_IN_CHIPS = 0.1
_GPS_DLL_AVERAGING_TIME_SEC = 20.0e-3
_AVERAGE_TRAVEL_TIME_SECONDS = 70.0e-3
_DEFAULT_MIN_CN0_DBHZ = 18.0
_DEFAULT_CONSTELLATION_TYPE_GPS = 1
_DEFAULT_TOW_DECODED_STATE_BIT = 3
_MIN_FIX_FIELDS = 8
_MIN_VALID_TOWS = 4
_MIN_VALID_OBSERVATIONS = 4


def _measurement_sigma_from_cn0(cn0_dbhz: float) -> float:
    snr = 10.0 ** (cn0_dbhz / 10.0)
    return (
        SPEED_OF_LIGHT_MPS
        * _GPS_CHIP_WIDTH_T_C_SEC
        * (_GPS_CORRELATOR_SPACING_IN_CHIPS / (4.0 * _GPS_DLL_AVERAGING_TIME_SEC * snr)) ** 0.5
    )


def _split_csv_like(line: str) -> list[str]:
    return [part.strip() for part in line.strip().split(",")]


def _parse_fix_record(fields: list[str]) -> FixRecord | None:
    if len(fields) < _MIN_FIX_FIELDS:
        return None
    return FixRecord(
        latitude_deg=float(fields[2]),
        longitude_deg=float(fields[3]),
        altitude_m=float(fields[4]),
        utc_time_ms=int(float(fields[7])),
    )


def _parse_raw_row(
    raw_columns: list[str],
    line: str,
    *,
    min_cn0_dbhz: float,
    constellation_type_gps: int,
    tow_decoded_state_bit: int,
) -> dict[str, str] | None:
    values = _split_csv_like(line)
    if len(values) < len(raw_columns):
        values.extend([""] * (len(raw_columns) - len(values)))
    row = {raw_columns[i]: values[i] for i in range(len(raw_columns))}
    try:
        constellation = int(row.get("ConstellationType", "0") or "0")
        state = int(row.get("State", "0") or "0")
        cn0 = float(row.get("Cn0DbHz", "0") or "0")
    except ValueError:
        return None
    tow_decoded = (state & (1 << tow_decoded_state_bit)) != 0
    if constellation != constellation_type_gps or (not tow_decoded) or cn0 < min_cn0_dbhz:
        return None
    return row


def _append_logger_line(  # noqa: C901, PLR0913, PLR0911
    line: str,
    raw_columns: list[str] | None,
    epochs_raw: dict[int, list[dict[str, str]]],
    fixes: list[FixRecord],
    *,
    min_cn0_dbhz: float,
    constellation_type_gps: int,
    tow_decoded_state_bit: int,
) -> list[str] | None:
    if not line:
        return raw_columns
    if line.startswith("# Raw,"):
        return [col.strip() for col in _split_csv_like(line[2:])]
    if line.startswith("#"):
        return raw_columns
    if line.startswith("Fix,"):
        fix = _parse_fix_record(_split_csv_like(line))
        if fix is not None:
            fixes.append(fix)
        return raw_columns
    if not line.startswith("Raw,") or raw_columns is None:
        return raw_columns

    row = _parse_raw_row(
        raw_columns,
        line,
        min_cn0_dbhz=min_cn0_dbhz,
        constellation_type_gps=constellation_type_gps,
        tow_decoded_state_bit=tow_decoded_state_bit,
    )
    if row is None:
        return raw_columns

    try:
        time_nanos = int(row.get("TimeNanos", "0") or "0")
    except ValueError:
        return raw_columns

    epochs_raw.setdefault(time_nanos, []).append(row)
    return raw_columns


def _rows_to_epoch(time_nanos: int, rows: list[dict[str, str]], gps_week: int) -> EpochMeasurements | None:
    tows: list[int] = []
    for row in rows:
        try:
            tows.append(int(float(row["ReceivedSvTimeNanos"])))
        except (KeyError, ValueError):
            continue
    if len(tows) < _MIN_VALID_TOWS:
        return None

    largest_tow_ns = max(tows)
    observations: list[SatelliteObservation] = []
    for row in rows:
        try:
            svid = int(float(row["Svid"]))
            cn0 = float(row["Cn0DbHz"])
            sv_tow_ns = int(float(row["ReceivedSvTimeNanos"]))
        except (KeyError, ValueError):
            continue

        delta_i_ns = largest_tow_ns - sv_tow_ns
        pseudorange_m = (_AVERAGE_TRAVEL_TIME_SECONDS + delta_i_ns * _SECONDS_PER_NANO) * SPEED_OF_LIGHT_MPS
        sigma_m = _measurement_sigma_from_cn0(cn0)
        observations.append(
            SatelliteObservation(
                svid=svid,
                pseudorange_m=pseudorange_m,
                sigma_m=sigma_m,
                cn0_dbhz=cn0,
                received_sv_time_ns=sv_tow_ns,
            )
        )

    if len(observations) < _MIN_VALID_OBSERVATIONS:
        return None

    return EpochMeasurements(
        time_nanos=time_nanos,
        receiver_tow_s=largest_tow_ns * _SECONDS_PER_NANO,
        gps_week=gps_week,
        observations=observations,
    )


def _build_epochs(epochs_raw: dict[int, list[dict[str, str]]], gps_week: int) -> list[EpochMeasurements]:
    epochs: list[EpochMeasurements] = []
    for time_nanos in sorted(epochs_raw):
        epoch = _rows_to_epoch(time_nanos, epochs_raw[time_nanos], gps_week)
        if epoch is not None:
            epochs.append(epoch)
    return epochs


def parse_gnss_logger_file(
    path,
    *,
    gps_week: int,
    min_cn0_dbhz: float = _DEFAULT_MIN_CN0_DBHZ,
    constellation_type_gps: int = _DEFAULT_CONSTELLATION_TYPE_GPS,
    tow_decoded_state_bit: int = _DEFAULT_TOW_DECODED_STATE_BIT,
) -> tuple[list[EpochMeasurements], list[FixRecord]]:
    """Parse a GNSS Logger file into epochs and position fixes."""
    raw_columns: list[str] | None = None
    epochs_raw: dict[int, list[dict[str, str]]] = {}
    fixes: list[FixRecord] = []

    for line in Path(path).read_text(encoding="utf-8", errors="ignore").splitlines():
        raw_columns = _append_logger_line(
            line,
            raw_columns,
            epochs_raw,
            fixes,
            min_cn0_dbhz=min_cn0_dbhz,
            constellation_type_gps=constellation_type_gps,
            tow_decoded_state_bit=tow_decoded_state_bit,
        )

    return _build_epochs(epochs_raw, gps_week), fixes
