# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\risk\test_var.py
# Module          : unit.risk.test_var
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for var module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for VaR."""

from __future__ import annotations

from src.risk.var import var_alpha


def test_var_alpha_returns_quantile() -> None:
    assert var_alpha([1, 2, 3, 4, 5], 0.8) == 4
