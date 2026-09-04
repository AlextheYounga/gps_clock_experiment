"""Regression tests for VSL frame-conversion helpers."""

from __future__ import annotations

import math
import unittest

from src.constants import F_RELATIVISTIC, OMEGA_E_DOT_RAD_S
from src.models import Ephemeris
from src.vsl.corrections import (
    earth_rotation_velocity_mps,
    ecef_to_inertial_velocity_mps,
    gravity_signal_time_shift_s,
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


class VslGravitySignalCorrectionTests(unittest.TestCase):
    """Validate the VSL gravity-induced signal frequency/time term."""

    @staticmethod
    def _ephemeris(eccentricity: float) -> Ephemeris:
        return Ephemeris(
            prn=1,
            week=0,
            toc=0.0,
            toe=0.0,
            af0=0.0,
            af1=0.0,
            af2=0.0,
            iode=0.0,
            crs=0.0,
            delta_n=0.0,
            m0=0.0,
            cuc=0.0,
            e=eccentricity,
            cus=0.0,
            root_a=math.sqrt(26_560_000.0),
            cic=0.0,
            omega0=0.0,
            cis=0.0,
            i0=0.0,
            crc=0.0,
            omega=0.0,
            omega_dot=0.0,
            i_dot=0.0,
            tgd=0.0,
            iodc=0.0,
        )

    def test_gravity_signal_time_shift_is_zero_for_circular_orbit(self) -> None:
        shift_s = gravity_signal_time_shift_s(self._ephemeris(0.0), math.pi / 2.0)

        self.assertEqual(shift_s, 0.0)

    def test_gravity_signal_time_shift_matches_half_standard_eccentricity_term(self) -> None:
        ephemeris = self._ephemeris(0.01)
        eccentric_anomaly_rad = 0.8

        shift_s = gravity_signal_time_shift_s(ephemeris, eccentric_anomaly_rad)
        half_standard_term_s = (
            0.5
            * F_RELATIVISTIC
            * ephemeris.e
            * ephemeris.root_a
            * math.sin(eccentric_anomaly_rad)
        )

        self.assertAlmostEqual(shift_s, half_standard_term_s, places=15)


if __name__ == "__main__":
    unittest.main()
