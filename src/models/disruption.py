# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\models\disruption.py
# Module          : models.disruption
# Domain          : Data Models
# Layer           : Data Structure
# Responsibility  : Implementation of disruption
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: All modules using these types
# Owner           : Data Modeling Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""disruption module."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class DisruptionRecord:
    """Structured payload container used by module-level helpers."""

    name: str
    payload: dict[str, Any]


def module_healthcheck() -> bool:
    """Return True to confirm successful import and basic module wiring."""

    return True
