# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\reliability_router.py
# Module          : algorithms.reliability_router
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of reliability router
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Reliability-aware ranking for candidate paths."""

from __future__ import annotations

from src.models.path import PathResult
from src.risk.reliability import reliability_probability


def rank_by_reliability(candidates: list[PathResult], tau: float) -> list[PathResult]:
    """Rank candidates by empirical reliability from synthetic sample approximation."""

    ranked: list[PathResult] = []
    for candidate in candidates:
        baseline = candidate.expected_cost if candidate.expected_cost is not None else candidate.cost
        samples = [baseline * factor for factor in (0.9, 1.0, 1.1, 1.2, 0.95)]
        candidate.reliability = reliability_probability(samples, tau)
        ranked.append(candidate)
    return sorted(ranked, key=lambda item: item.reliability or 0.0, reverse=True)
