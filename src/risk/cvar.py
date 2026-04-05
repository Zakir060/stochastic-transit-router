# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\risk\cvar.py
# Module          : risk.cvar
# Domain          : Risk Analysis
# Layer           : Analysis
# Responsibility  : Implementation of cvar
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Conditional Value at Risk estimation."""

from __future__ import annotations

from src.risk.var import var_alpha


def cvar_alpha(samples: list[float], alpha: float) -> float:
    """Return empirical CVaR at confidence alpha."""

    if not samples:
        return 0.0
    threshold = var_alpha(samples, alpha)
    tail = [sample for sample in samples if sample >= threshold]
    return sum(tail) / len(tail) if tail else threshold
