"""Regression tests for VSL frame-conversion helpers."""

from __future__ import annotations

import math
import unittest

from src.constants import OMEGA_E_DOT_RAD_S, SPEED_OF_LIGHT_MPS as EMISSION_SPEED_MPS
from src.vsl.corrections import (
    earth_rotation_velocity_mps,
    ecef_to_inertial_velocity_mps,
    effective_light_speed_mps,
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


class VslNewtonianGravityLightTests(unittest.TestCase):
    """Validate the Newtonian corpuscle light-speed model."""

    def test_falling_light_speeds_up_and_rising_light_slows_down(self) -> None:
        satellite_radius_m = 26_560_000.0
        receiver_radius_m = 6_371_000.0

        falling_mps = effective_light_speed_mps(satellite_radius_m, receiver_radius_m)
        rising_mps = effective_light_speed_mps(receiver_radius_m, satellite_radius_m)

        self.assertGreater(falling_mps, EMISSION_SPEED_MPS)
        self.assertLess(rising_mps, EMISSION_SPEED_MPS)

    def test_equal_radii_give_the_emission_speed(self) -> None:
        radius_m = 26_560_000.0

        speed_mps = effective_light_speed_mps(radius_m, radius_m)

        self.assertEqual(speed_mps, EMISSION_SPEED_MPS)


if __name__ == "__main__":
    unittest.main()
