# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\risk\var.py
# Module          : risk.var
# Domain          : Risk Analysis
# Layer           : Analysis
# Responsibility  : Implementation of var
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Value at Risk estimation."""

from __future__ import annotations


def var_alpha(samples: list[float], alpha: float) -> float:
    """Return empirical VaR at confidence alpha."""

    if not samples:
        return 0.0
    ordered = sorted(samples)
    idx = min(max(int(alpha * (len(ordered) - 1)), 0), len(ordered) - 1)
    return ordered[idx]
