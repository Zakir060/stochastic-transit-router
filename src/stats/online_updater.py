# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\stats\online_updater.py
# Module          : stats.online_updater
# Domain          : Statistics
# Layer           : Analysis
# Responsibility  : Implementation of online updater
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service, evaluation
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Online parameter update utilities with EMA."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class OnlineMoments:
    """Maintain EMA mean and variance updates."""

    alpha: float
    mean: float = 0.0
    variance: float = 0.0

    def update(self, observation: float) -> None:
        """Update EMA mean and variance with one observation."""

        new_mean = self.alpha * observation + (1 - self.alpha) * self.mean
        new_variance = self.alpha * (observation - new_mean) ** 2 + (1 - self.alpha) * self.variance
        self.mean = new_mean
        self.variance = new_variance
