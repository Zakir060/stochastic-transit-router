# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\risk\scorer.py
# Module          : risk.scorer
# Domain          : Risk Analysis
# Layer           : Analysis
# Responsibility  : Implementation of scorer
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Risk-aware route scoring."""

from __future__ import annotations

import math


def mean_variance_score(expected: float, variance: float, risk_lambda: float) -> float:
    """Return mean variance score."""

    sigma = math.sqrt(variance) if variance > 0 else 0.0
    return expected + risk_lambda * sigma
