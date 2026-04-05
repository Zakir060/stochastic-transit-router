# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\models\distribution.py
# Module          : models.distribution
# Domain          : Data Models
# Layer           : Data Structure
# Responsibility  : Implementation of distribution
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: All modules using these types
# Owner           : Data Modeling Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Empirical travel-time distribution helpers."""

from __future__ import annotations

from dataclasses import dataclass
import statistics


@dataclass(slots=True)
class EmpiricalDistribution:
    """Simple empirical distribution backed by observed samples."""

    samples: list[float]

    def mean(self) -> float:
        """Return empirical mean."""

        return statistics.fmean(self.samples) if self.samples else 0.0

    def variance(self) -> float:
        """Return population variance."""

        return statistics.pvariance(self.samples) if len(self.samples) > 1 else 0.0

    def cdf(self, value: float) -> float:
        """Return empirical cumulative probability at value."""

        if not self.samples:
            return 0.0
        count = sum(1 for sample in self.samples if sample <= value)
        return count / len(self.samples)

    def quantile(self, alpha: float) -> float:
        """Return empirical alpha quantile."""

        if not self.samples:
            return 0.0
        ordered = sorted(self.samples)
        index = min(max(int(alpha * (len(ordered) - 1)), 0), len(ordered) - 1)
        return ordered[index]
