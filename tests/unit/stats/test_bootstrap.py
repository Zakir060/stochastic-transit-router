# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\stats\test_bootstrap.py
# Module          : unit.stats.test_bootstrap
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for bootstrap module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for bootstrap confidence interval."""

from __future__ import annotations

from src.stats.bootstrap import bootstrap_mean_ci


def test_bootstrap_ci_bounds_order() -> None:
    low, high = bootstrap_mean_ci([1, 2, 3, 4, 5], iterations=200, alpha=0.1)
    assert low <= high
