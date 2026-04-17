from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SPEED_OF_LIGHT_MPS = 299792458.0
SECONDS_PER_NANO = 1e-9
GPS_CHIP_WIDTH_T_C_SEC = 1.0e-6
GPS_CORRELATOR_SPACING_IN_CHIPS = 0.1
GPS_DLL_AVERAGING_TIME_SEC = 20.0e-3
AVERAGE_TRAVEL_TIME_SECONDS = 70.0e-3


@dataclass(frozen=True)
class SatelliteObservation:
    svid: int
    pseudorange_m: float
    sigma_m: float
    cn0_dbhz: float
    received_sv_time_ns: int


@dataclass(frozen=True)
class EpochMeasurements:
    time_nanos: int
    receiver_tow_s: float
    gps_week: int
    observations: list[SatelliteObservation]


@dataclass(frozen=True)
class FixRecord:
    latitude_deg: float
    longitude_deg: float
    altitude_m: float
    utc_time_ms: int


@dataclass(frozen=True)
class Ephemeris:
    prn: int
    week: int
    toc: float
    toe: float
    af0: float
    af1: float
    af2: float
    iode: float
    crs: float
    delta_n: float
    m0: float
    cuc: float
    e: float
    cus: float
    root_a: float
    cic: float
    omega0: float
    cis: float
    i0: float
    crc: float
    omega: float
    omega_dot: float
    i_dot: float
    tgd: float
    iodc: float


def _parse_float_token(token: str) -> float:
    text = token.strip().replace("D", "E")
    if not text:
        return 0.0
    return float(text)


def _fixed_width_fields(line: str, start: int, width: int, count: int) -> list[float]:
    out: list[float] = []
    for i in range(count):
        token = line[start + i * width : start + (i + 1) * width]
        out.append(_parse_float_token(token))
    return out


def parse_rinex_nav_file(path: str | Path) -> dict[int, list[Ephemeris]]:
    file_path = Path(path)
    lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()

    idx = 0
    while idx < len(lines) and "END OF HEADER" not in lines[idx]:
        idx += 1
    idx += 1

    by_prn: dict[int, list[Ephemeris]] = {}

    while idx + 7 < len(lines):
        block = lines[idx : idx + 8]
        if not block[0].strip():
            idx += 1
            continue

        try:
            prn = int(block[0][0:2])
        except ValueError:
            idx += 1
            continue

        year = int(block[0][3:5])
        month = int(block[0][6:8])
        day = int(block[0][9:11])
        hour = int(block[0][12:14])
        minute = int(block[0][15:17])
        second = float(block[0][18:22])
        _ = (year, month, day)
        toc = hour * 3600.0 + minute * 60.0 + second

        af0, af1, af2 = _fixed_width_fields(block[0], 22, 19, 3)
        l2 = _fixed_width_fields(block[1], 3, 19, 4)
        l3 = _fixed_width_fields(block[2], 3, 19, 4)
        l4 = _fixed_width_fields(block[3], 3, 19, 4)
        l5 = _fixed_width_fields(block[4], 3, 19, 4)
        l6 = _fixed_width_fields(block[5], 3, 19, 4)
        l7 = _fixed_width_fields(block[6], 3, 19, 4)

        eph = Ephemeris(
            prn=prn,
            week=int(round(l6[2])),
            toc=toc,
            toe=l4[0],
            af0=af0,
            af1=af1,
            af2=af2,
            iode=l2[0],
            crs=l2[1],
            delta_n=l2[2],
            m0=l2[3],
            cuc=l3[0],
            e=l3[1],
            cus=l3[2],
            root_a=l3[3],
            cic=l4[1],
            omega0=l4[2],
            cis=l4[3],
            i0=l5[0],
            crc=l5[1],
            omega=l5[2],
            omega_dot=l5[3],
            i_dot=l6[0],
            tgd=l7[2],
            iodc=l7[3],
        )
        by_prn.setdefault(prn, []).append(eph)
        idx += 8

    return by_prn


def _measurement_sigma_from_cn0(cn0_dbhz: float) -> float:
    signal_to_noise_ratio_linear = 10.0 ** (cn0_dbhz / 10.0)
    return (
        SPEED_OF_LIGHT_MPS
        * GPS_CHIP_WIDTH_T_C_SEC
        * (GPS_CORRELATOR_SPACING_IN_CHIPS / (4.0 * GPS_DLL_AVERAGING_TIME_SEC * signal_to_noise_ratio_linear)) ** 0.5
    )


def _split_csv_like(line: str) -> list[str]:
    return [part.strip() for part in line.strip().split(",")]


def parse_gnss_logger_file(
    path: str | Path,
    *,
    gps_week: int,
    min_cn0_dbhz: float = 18.0,
    constellation_type_gps: int = 1,
    tow_decoded_state_bit: int = 3,
) -> tuple[list[EpochMeasurements], list[FixRecord]]:
    raw_columns: list[str] | None = None
    epochs_raw: dict[int, list[dict[str, str]]] = {}
    fixes: list[FixRecord] = []

    for line in Path(path).read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line:
            continue
        if line.startswith("# Raw,"):
            raw_columns = [col.strip() for col in _split_csv_like(line[2:])]
            continue
        if line.startswith("#"):
            continue

        if line.startswith("Fix,"):
            fields = _split_csv_like(line)
            if len(fields) >= 8:
                fixes.append(
                    FixRecord(
                        latitude_deg=float(fields[2]),
                        longitude_deg=float(fields[3]),
                        altitude_m=float(fields[4]),
                        utc_time_ms=int(float(fields[7])),
                    )
                )
            continue

        if not line.startswith("Raw,"):
            continue

        values = _split_csv_like(line)
        if raw_columns is None:
            continue
        if len(values) < len(raw_columns):
            values.extend([""] * (len(raw_columns) - len(values)))

        row = {raw_columns[i]: values[i] for i in range(len(raw_columns))}

        try:
            constellation = int(row.get("ConstellationType", "0") or "0")
            state = int(row.get("State", "0") or "0")
            cn0 = float(row.get("Cn0DbHz", "0") or "0")
            time_nanos = int(row.get("TimeNanos", "0") or "0")
        except ValueError:
            continue

        tow_decoded = (state & (1 << tow_decoded_state_bit)) != 0
        if constellation != constellation_type_gps or (not tow_decoded) or cn0 < min_cn0_dbhz:
            continue

        epochs_raw.setdefault(time_nanos, []).append(row)

    epochs: list[EpochMeasurements] = []
    for time_nanos in sorted(epochs_raw):
        rows = epochs_raw[time_nanos]
        tows = []
        for row in rows:
            try:
                tows.append(int(float(row["ReceivedSvTimeNanos"])))
            except (KeyError, ValueError):
                continue
        if len(tows) < 4:
            continue

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
            pseudorange_m = (AVERAGE_TRAVEL_TIME_SECONDS + delta_i_ns * SECONDS_PER_NANO) * SPEED_OF_LIGHT_MPS
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

        if len(observations) < 4:
            continue

        epochs.append(
            EpochMeasurements(
                time_nanos=time_nanos,
                receiver_tow_s=largest_tow_ns * SECONDS_PER_NANO,
                gps_week=gps_week,
                observations=observations,
            )
        )

    return epochs, fixes


def iter_all_ephemerides(nav_by_prn: dict[int, list[Ephemeris]]) -> Iterable[Ephemeris]:
    for eph_list in nav_by_prn.values():
        for eph in eph_list:
            yield eph
