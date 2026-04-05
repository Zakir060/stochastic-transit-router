# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\risk\test_reliability.py
# Module          : unit.risk.test_reliability
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for reliability module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for reliability probability."""

from __future__ import annotations

from src.risk.reliability import reliability_probability


def test_reliability_probability_matches_fraction() -> None:
    assert reliability_probability([5, 10, 15, 20], 12) == 0.5
