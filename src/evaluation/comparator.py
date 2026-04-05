# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\evaluation\comparator.py
# Module          : evaluation.comparator
# Domain          : Evaluation
# Layer           : Research
# Responsibility  : Implementation of comparator
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
# File            : src/evaluation/comparator.py
# Module          : evaluation.comparator
# Domain          : Evaluation
# Layer           : Research
# Responsibility  : Compare routes and algorithms
# Public Surface  : Comparison interfaces
# Primary Inputs  : Multiple route solutions
# Primary Outputs : Comparison results
# Primary Consumers: Analysis, reporting
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Module comparator.
"""Module comparator.

This module is part of the stochastic-transit-router production codebase.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ComparatorRecord:
    """Structured payload container used by module-level helpers."""

    name: str
    payload: dict[str, Any]


def module_healthcheck() -> bool:
    """Return True to confirm successful import and basic module wiring."""

    return True
