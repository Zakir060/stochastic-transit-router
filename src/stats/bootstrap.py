# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\stats\bootstrap.py
# Module          : stats.bootstrap
# Domain          : Statistics
# Layer           : Analysis
# Responsibility  : Implementation of bootstrap
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service, evaluation
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Bootstrap confidence interval utilities."""

from __future__ import annotations

import random
import statistics


def bootstrap_mean_ci(samples: list[float], iterations: int = 1000, alpha: float = 0.05, seed: int = 20260405) -> tuple[float, float]:
    """Return percentile bootstrap confidence interval for sample mean."""

    if not samples:
        return (0.0, 0.0)

    rng = random.Random(seed)
    n = len(samples)
    means: list[float] = []
    for _ in range(iterations):
        draw = [samples[rng.randrange(n)] for _ in range(n)]
        means.append(statistics.fmean(draw))
    means.sort()
    low_idx = int((alpha / 2) * (iterations - 1))
    high_idx = int((1 - alpha / 2) * (iterations - 1))
    return (means[low_idx], means[high_idx])
