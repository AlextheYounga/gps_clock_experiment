"""CSL model configuration."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CslConfig:
    """Configuration for the standard CSL solver run."""

    @property
    def enable_relativistic_eccentricity(self) -> bool:
        """Return whether the relativistic eccentricity term is enabled."""
        return True

    @property
    def label(self) -> str:
        """Return the human-readable solver label."""
        return "CSL/STANDARD"


# Presets
STANDARD_CONFIG = CslConfig()
