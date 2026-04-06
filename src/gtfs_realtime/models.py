# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\gtfs_realtime\models.py
# Module          : gtfs_realtime.models
# Domain          : GTFS-Realtime
# Layer           : Data Processing
# Responsibility  : Implementation of models
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Realtime updates, API
# Owner           : Data Processing Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src/gtfs_realtime/models.py
# Module          : gtfs_realtime.models
# Domain          : GTFS-Realtime
# Layer           : Data Structure
# Responsibility  : Define data models for GTFS-Realtime entities
# Public Surface  : Realtime entity classes
# Primary Inputs  : Parsed realtime data
# Primary Outputs : Structured realtime models
# Primary Consumers: All realtime processing modules
# Owner           : Data Processing Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""models module."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ModelsRecord:
    """Structured payload container used by module-level helpers."""

    name: str
    payload: dict[str, Any]


def module_healthcheck() -> bool:
    """Return True to confirm successful import and basic module wiring."""

    return True
