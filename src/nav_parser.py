"""RINEX navigation file parser."""

from __future__ import annotations

from pathlib import Path

from src.models import Ephemeris


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
    """Parse a RINEX v2 GPS navigation file into ephemerides grouped by PRN."""
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

        hour = int(block[0][12:14])
        minute = int(block[0][15:17])
        second = float(block[0][18:22])
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
            week=round(l6[2]),
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
