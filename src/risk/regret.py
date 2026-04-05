# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\risk\regret.py
# Module          : risk.regret
# Domain          : Risk Analysis
# Layer           : Analysis
# Responsibility  : Implementation of regret
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Regret metric calculations."""

from __future__ import annotations


def regret(realized_value: float, realized_alternatives: list[float]) -> float:
    """Return regret relative to best realized alternative."""

    if not realized_alternatives:
        return 0.0
    return realized_value - min(realized_alternatives)
