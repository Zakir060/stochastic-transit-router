# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\stats\empirical_cdf.py
# Module          : stats.empirical_cdf
# Domain          : Statistics
# Layer           : Analysis
# Responsibility  : Implementation of empirical cdf
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service, evaluation
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Empirical CDF estimators."""

from __future__ import annotations


def empirical_cdf(samples: list[float], value: float) -> float:
    """Return empirical cumulative probability at value."""

    if not samples:
        return 0.0
    count = sum(1 for sample in samples if sample <= value)
    return count / len(samples)


def cdf_curve(samples: list[float]) -> list[tuple[float, float]]:
    """Return sorted points of empirical CDF."""

    if not samples:
        return []
    ordered = sorted(samples)
    n = len(ordered)
    return [(value, idx / n) for idx, value in enumerate(ordered, start=1)]
