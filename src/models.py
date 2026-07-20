"""Shared dataclasses for GNSS measurements and navigation data.

These types are model-neutral and safe to import from both csl/ and vsl/.
They carry no propagation or clock-correction assumptions.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SatelliteObservation:
    """A single satellite pseudorange observation."""

    svid: int
    pseudorange_m: float
    sigma_m: float
    cn0_dbhz: float
    received_sv_time_ns: int


@dataclass(frozen=True)
class EpochMeasurements:
    """All observations captured for one receiver epoch."""

    time_nanos: int
    receiver_tow_s: float
    gps_week: int
    observations: list[SatelliteObservation]


@dataclass(frozen=True)
class FixRecord:
    """A position fix reported by the GNSS logger."""

    latitude_deg: float
    longitude_deg: float
    altitude_m: float
    utc_time_ms: int


@dataclass(frozen=True)
class Ephemeris:
    """Parsed broadcast ephemeris parameters for one satellite."""

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
