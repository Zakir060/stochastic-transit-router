# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\risk\test_scorer.py
# Module          : unit.risk.test_scorer
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for scorer module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for mean variance scorer."""

from __future__ import annotations

from src.risk.scorer import mean_variance_score


def test_mean_variance_score_increases_with_lambda() -> None:
    low = mean_variance_score(10, 4, 0.0)
    high = mean_variance_score(10, 4, 2.0)
    assert high > low
