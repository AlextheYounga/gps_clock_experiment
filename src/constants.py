"""Physical and calendar constants shared across all model packages.

Only constants that are genuinely model-neutral belong here.

Design note on SPEED_OF_LIGHT_MPS:
  The nominal value 299792458.0 m/s is the ICD-GPS-200 reference value.
  It is listed here as a shared unit and ICD constant.
  Each model package is responsible for deciding how this value enters
  its propagation equations. Neither CSL nor VSL should silently rely
  on this value being the assumed propagation speed without an explicit
  architectural choice in the model package itself.
"""

from __future__ import annotations

# ICD-GPS-200 nominal speed of light (m/s)
SPEED_OF_LIGHT_MPS: float = 299792458.0

# Earth gravitational parameter (m^3/s^2) — ICD-GPS-200
MU_M3_S2: float = 3.986005e14

# Relativistic clock correction constant F (s / sqrt(m)) — ICD-GPS-200
F_RELATIVISTIC: float = -4.442807633e-10

# Earth rotation rate (rad/s) — ICD-GPS-200
OMEGA_E_DOT_RAD_S: float = 7.2921151467e-5

# GPS week duration (seconds)
SECONDS_IN_WEEK: int = 604800

# WGS84 ellipsoid semi-major axis (m)
WGS84_A: float = 6378137.0

# WGS84 first eccentricity squared
WGS84_E2: float = 6.69437999014e-3
