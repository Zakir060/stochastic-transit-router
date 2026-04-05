# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\risk\reliability.py
# Module          : risk.reliability
# Domain          : Risk Analysis
# Layer           : Analysis
# Responsibility  : Implementation of reliability
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Reliability metric utilities."""

from __future__ import annotations


def reliability_probability(samples: list[float], tau: float) -> float:
    """Return probability that travel time is under threshold tau."""

    if not samples:
        return 0.0
    return sum(1 for sample in samples if sample <= tau) / len(samples)
