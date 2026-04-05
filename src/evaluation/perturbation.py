# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\evaluation\perturbation.py
# Module          : evaluation.perturbation
# Domain          : Evaluation
# Layer           : Research
# Responsibility  : Implementation of perturbation
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
# File            : src/evaluation/perturbation.py
# Module          : evaluation.perturbation
# Domain          : Evaluation
# Layer           : Research
# Responsibility  : Generate perturbations for sensitivity analysis
# Public Surface  : Perturbation generation interfaces
# Primary Inputs  : Base scenario data
# Primary Outputs : Perturbed scenarios
# Primary Consumers: Experiment runner, robustness testing
# Owner           : Research Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Module perturbation.
"""Module perturbation.

This module is part of the stochastic-transit-router production codebase.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class PerturbationRecord:
    """Structured payload container used by module-level helpers."""

    name: str
    payload: dict[str, Any]


def module_healthcheck() -> bool:
    """Return True to confirm successful import and basic module wiring."""

    return True
