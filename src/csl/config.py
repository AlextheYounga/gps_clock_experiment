"""CSL model configuration."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class ClockModel(Enum):
    """Satellite clock correction variant for the CSL solver."""

    STANDARD = auto()
    """Full ICD clock correction including relativistic eccentricity term."""

    NO_RELATIVISTIC_ECCENTRICITY = auto()
    """Polynomial-only clock correction; ablation test removing F*e*sqrt(A)*sin(E)."""


@dataclass(frozen=True)
class CslConfig:
    """Full configuration for one CSL solver run."""

    clock_model: ClockModel = ClockModel.STANDARD

    @property
    def enable_relativistic_eccentricity(self) -> bool:
        return self.clock_model == ClockModel.STANDARD

    @property
    def label(self) -> str:
        return f"CSL/{self.clock_model.name}"


# Presets
STANDARD_CONFIG = CslConfig(clock_model=ClockModel.STANDARD)
NO_RELATIVITY_CONFIG = CslConfig(clock_model=ClockModel.NO_RELATIVISTIC_ECCENTRICITY)
