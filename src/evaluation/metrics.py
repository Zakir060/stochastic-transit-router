# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\evaluation\metrics.py
# Module          : evaluation.metrics
# Domain          : Evaluation
# Layer           : Research
# Responsibility  : Implementation of metrics
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Experiment runner, notebooks
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src/evaluation/metrics.py
# Module          : evaluation.metrics
# Domain          : Evaluation
# Layer           : Research
# Responsibility  : Compute evaluation metrics for route quality
# Public Surface  : Metric computation interfaces
# Primary Inputs  : Routes and ground truth data
# Primary Outputs : Evaluation metrics
# Primary Consumers: Comparator, reporting
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Module metrics.
"""Module metrics.

This module is part of the stochastic-transit-router production codebase.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class MetricsRecord:
    """Structured payload container used by module-level helpers."""

    name: str
    payload: dict[str, Any]


def module_healthcheck() -> bool:
    """Return True to confirm successful import and basic module wiring."""

    return True
