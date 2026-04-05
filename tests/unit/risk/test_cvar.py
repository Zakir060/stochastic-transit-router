# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\risk\test_cvar.py
# Module          : unit.risk.test_cvar
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for cvar module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for CVaR."""

from __future__ import annotations

from src.risk.cvar import cvar_alpha


def test_cvar_alpha_tail_average() -> None:
    value = cvar_alpha([1, 2, 3, 4, 5], 0.8)
    assert value >= 4
