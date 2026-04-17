"""VSL model configuration."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class BallisticVariant(Enum):
    """Which ballistic propagation variant to use."""

    FULL_VECTOR = auto()
    """Full source-velocity inheritance with moving-receiver interception."""


@dataclass(frozen=True)
class VslConfig:
    """Full configuration for one VSL solver run."""

    variant: BallisticVariant = BallisticVariant.FULL_VECTOR

    @property
    def label(self) -> str:
        return f"VSL/{self.variant.name}"


# Presets
BALLISTIC_FULL_VECTOR_CONFIG = VslConfig(variant=BallisticVariant.FULL_VECTOR)
