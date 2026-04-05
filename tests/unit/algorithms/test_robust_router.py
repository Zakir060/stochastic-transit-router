# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\algorithms\test_robust_router.py
# Module          : unit.algorithms.test_robust_router
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for robust_router module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for robust ranking."""

from __future__ import annotations

from src.algorithms.robust_router import rank_by_robust_score
from src.models.path import PathResult


def test_robust_score_orders_low_risk_first() -> None:
    candidates = [
        PathResult(nodes=["A", "B"], cost=0, expected_cost=10, variance=1),
        PathResult(nodes=["A", "C"], cost=0, expected_cost=9, variance=9),
    ]
    ranked = rank_by_robust_score(candidates, 1.0)
    assert ranked[0].nodes == ["A", "B"]
