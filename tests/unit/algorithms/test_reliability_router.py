# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\algorithms\test_reliability_router.py
# Module          : unit.algorithms.test_reliability_router
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for reliability_router module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for reliability ranking."""

from __future__ import annotations

from src.algorithms.reliability_router import rank_by_reliability
from src.models.path import PathResult


def test_reliability_ranking_descending() -> None:
    candidates = [PathResult(nodes=["A", "B"], cost=10, expected_cost=10), PathResult(nodes=["A", "C"], cost=20, expected_cost=20)]
    ranked = rank_by_reliability(candidates, 12)
    assert ranked[0].expected_cost == 10
