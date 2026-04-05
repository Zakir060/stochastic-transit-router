# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\robust_router.py
# Module          : algorithms.robust_router
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of robust router
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Mean variance robust route ranking."""

from __future__ import annotations

from src.models.path import PathResult
from src.risk.scorer import mean_variance_score


def rank_by_robust_score(candidates: list[PathResult], risk_lambda: float) -> list[PathResult]:
    """Rank candidates by mean variance score."""

    for candidate in candidates:
        expected = candidate.expected_cost if candidate.expected_cost is not None else candidate.cost
        variance = candidate.variance if candidate.variance is not None else 0.0
        candidate.cost = mean_variance_score(expected, variance, risk_lambda)
    return sorted(candidates, key=lambda item: item.cost)
