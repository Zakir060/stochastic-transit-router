# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\algorithms\test_cvar_router.py
# Module          : unit.algorithms.test_cvar_router
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for cvar_router module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for CVaR selection."""

from __future__ import annotations

from src.algorithms.cvar_router import select_min_cvar_path
from src.models.path import PathResult


def test_cvar_selects_lower_tail_candidate() -> None:
    candidates = [PathResult(nodes=["A", "B"], cost=0, expected_cost=8), PathResult(nodes=["A", "C"], cost=0, expected_cost=15)]
    selected = select_min_cvar_path(candidates, 0.95)
    assert selected is not None
    assert selected.nodes == ["A", "B"]
