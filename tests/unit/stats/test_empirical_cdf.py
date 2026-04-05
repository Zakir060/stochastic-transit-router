# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\stats\test_empirical_cdf.py
# Module          : unit.stats.test_empirical_cdf
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for empirical_cdf module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for empirical CDF."""

from __future__ import annotations

from src.stats.empirical_cdf import empirical_cdf


def test_empirical_cdf_expected_probability() -> None:
    samples = [1, 2, 3, 4]
    assert empirical_cdf(samples, 2) == 0.5
