# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\pareto_filter.py
# Module          : algorithms.pareto_filter
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of pareto filter
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Pareto filtering helpers for non-dominated path sets."""

from __future__ import annotations

from src.models.path import PathResult


def pareto_filter(candidates: list[PathResult]) -> list[PathResult]:
    """Return candidates not dominated by cost and variance."""

    survivors: list[PathResult] = []
    for candidate in candidates:
        dominated = False
        for other in candidates:
            if other is candidate:
                continue
            other_var = other.variance if other.variance is not None else 0.0
            candidate_var = candidate.variance if candidate.variance is not None else 0.0
            if other.cost <= candidate.cost and other_var <= candidate_var and (
                other.cost < candidate.cost or other_var < candidate_var
            ):
                dominated = True
                break
        if not dominated:
            survivors.append(candidate)
    return survivors
