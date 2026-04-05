# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\stats\outlier_handler.py
# Module          : stats.outlier_handler
# Domain          : Statistics
# Layer           : Analysis
# Responsibility  : Implementation of outlier handler
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service, evaluation
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Outlier filtering based on duration and speed policy."""

from __future__ import annotations


def filter_duration_and_speed(
    duration_seconds: list[float],
    speed_mph: list[float],
    min_duration: float = 60,
    max_duration: float = 10800,
    min_speed: float = 0.1,
    max_speed: float = 80,
) -> list[int]:
    """Return indices of valid observations under policy thresholds."""

    valid: list[int] = []
    for idx, (duration, speed) in enumerate(zip(duration_seconds, speed_mph, strict=True)):
        if min_duration <= duration <= max_duration and min_speed <= speed <= max_speed:
            valid.append(idx)
    return valid
