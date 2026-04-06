# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\utils\retry.py
# Module          : utils.retry
# Domain          : Utilities
# Layer           : Infrastructure
# Responsibility  : Implementation of retry
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: All modules
# Owner           : Infrastructure Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""retry module."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class RetryRecord:
    """Structured payload container used by module-level helpers."""

    name: str
    payload: dict[str, Any]


def module_healthcheck() -> bool:
    """Return True to confirm successful import and basic module wiring."""

    return True
