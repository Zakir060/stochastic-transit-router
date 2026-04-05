# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\cvar_router.py
# Module          : algorithms.cvar_router
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of cvar router
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""CVaR based route selection."""

from __future__ import annotations

from src.models.path import PathResult
from src.risk.cvar import cvar_alpha


def select_min_cvar_path(candidates: list[PathResult], alpha: float) -> PathResult | None:
    """Select candidate with minimum empirical CVaR estimate."""

    best: PathResult | None = None
    best_cvar = float("inf")
    for candidate in candidates:
        baseline = candidate.expected_cost if candidate.expected_cost is not None else candidate.cost
        samples = [baseline * factor for factor in (0.9, 1.0, 1.05, 1.15, 1.3)]
        candidate.cvar = cvar_alpha(samples, alpha)
        if candidate.cvar < best_cvar:
            best_cvar = candidate.cvar
            best = candidate
    return best
