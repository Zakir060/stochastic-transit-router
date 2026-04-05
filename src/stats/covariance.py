# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\stats\covariance.py
# Module          : stats.covariance
# Domain          : Statistics
# Layer           : Analysis
# Responsibility  : Implementation of covariance
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service, evaluation
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Covariance estimation with sparse fallback policy."""

from __future__ import annotations

import statistics


def covariance(x: list[float], y: list[float], min_obs: int = 30) -> float:
    """Return covariance or zero when observations are sparse."""

    n = min(len(x), len(y))
    if n < min_obs or n < 2:
        return 0.0
    mx = statistics.fmean(x[:n])
    my = statistics.fmean(y[:n])
    return sum((a - mx) * (b - my) for a, b in zip(x[:n], y[:n], strict=True)) / n
