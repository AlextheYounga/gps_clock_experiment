"""Regression tests for VSL frame-conversion helpers."""

from __future__ import annotations

import math
import unittest

from src.constants import OMEGA_E_DOT_RAD_S
from src.vsl.corrections import (
    earth_rotation_velocity_mps,
    ecef_to_inertial_velocity_mps,
    rotate_ecef_position_forward,
)


class VslFrameCorrectionTests(unittest.TestCase):
    """Validate ECEF and inertial frame conversions used by VSL propagation."""

    def test_ecef_to_inertial_velocity_adds_earth_rotation_component(self) -> None:
        position_m = (0.0, 26_560_000.0, 0.0)
        ecef_velocity_mps = (100.0, 200.0, 300.0)

        converted = ecef_to_inertial_velocity_mps(position_m, ecef_velocity_mps)

        self.assertAlmostEqual(converted[0], 100.0 - OMEGA_E_DOT_RAD_S * position_m[1])
        self.assertAlmostEqual(converted[1], 200.0)
        self.assertAlmostEqual(converted[2], 300.0)

    def test_receiver_rotation_and_velocity_use_the_same_positive_rotation(self) -> None:
        radius_m = 6_378_137.0
        quarter_turn_s = math.pi / (2.0 * OMEGA_E_DOT_RAD_S)

        rotated = rotate_ecef_position_forward((radius_m, 0.0, 0.0), quarter_turn_s)
        rotation_velocity = earth_rotation_velocity_mps((radius_m, 0.0, 0.0))

        self.assertAlmostEqual(rotated[0], 0.0, places=5)
        self.assertAlmostEqual(rotated[1], radius_m, places=5)
        self.assertAlmostEqual(rotation_velocity[0], 0.0)
        self.assertAlmostEqual(rotation_velocity[1], OMEGA_E_DOT_RAD_S * radius_m)


if __name__ == "__main__":
    unittest.main()
