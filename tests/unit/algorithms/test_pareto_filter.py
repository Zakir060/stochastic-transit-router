# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\algorithms\test_pareto_filter.py
# Module          : unit.algorithms.test_pareto_filter
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for pareto_filter module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for Pareto filtering."""

from __future__ import annotations

from src.algorithms.pareto_filter import pareto_filter
from src.models.path import PathResult


def test_pareto_filter_removes_dominated_path() -> None:
    candidates = [
        PathResult(nodes=["A", "B"], cost=10, variance=4),
        PathResult(nodes=["A", "C"], cost=12, variance=6),
    ]
    filtered = pareto_filter(candidates)
    assert len(filtered) == 1
    assert filtered[0].nodes == ["A", "B"]
