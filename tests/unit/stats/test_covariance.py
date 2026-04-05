# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\stats\test_covariance.py
# Module          : unit.stats.test_covariance
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for covariance module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for covariance estimator."""

from __future__ import annotations

from src.stats.covariance import covariance


def test_covariance_sparse_fallback_zero() -> None:
    assert covariance([1, 2], [3, 4], min_obs=5) == 0.0
