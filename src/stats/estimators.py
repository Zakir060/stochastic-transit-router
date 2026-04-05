# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\stats\estimators.py
# Module          : stats.estimators
# Domain          : Statistics
# Layer           : Analysis
# Responsibility  : Implementation of estimators
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service, evaluation
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Descriptive statistics estimators."""

from __future__ import annotations

import math
import statistics


def descriptive_summary(samples: list[float]) -> dict[str, float]:
    """Return descriptive statistics for a sample vector."""

    if not samples:
        return {
            "mean": 0.0,
            "median": 0.0,
            "std": 0.0,
            "skewness": 0.0,
            "kurtosis": 0.0,
        }

    mean = statistics.fmean(samples)
    median = statistics.median(samples)
    std = statistics.pstdev(samples) if len(samples) > 1 else 0.0
    if std == 0:
        skewness = 0.0
        kurtosis = 0.0
    else:
        centered = [(x - mean) / std for x in samples]
        skewness = sum(value ** 3 for value in centered) / len(centered)
        kurtosis = sum(value ** 4 for value in centered) / len(centered) - 3.0

    return {
        "mean": mean,
        "median": median,
        "std": std,
        "skewness": skewness,
        "kurtosis": kurtosis,
    }
