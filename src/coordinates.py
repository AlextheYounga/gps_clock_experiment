"""Model-neutral coordinate transforms and geometry helpers."""

from __future__ import annotations

import math

from src.constants import WGS84_A, WGS84_E2


def lla_to_ecef(latitude_deg: float, longitude_deg: float, altitude_m: float) -> tuple[float, float, float]:
    """Convert geodetic (WGS84) coordinates to ECEF (m)."""
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
    """Return Euclidean distance between two 3D points (m)."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
