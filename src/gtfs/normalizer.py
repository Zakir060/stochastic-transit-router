# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\gtfs\normalizer.py
# Module          : gtfs.normalizer
# Domain          : GTFS Processing
# Layer           : Data Processing
# Responsibility  : Implementation of normalizer
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Ingest pipeline
# Owner           : Data Processing Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src/gtfs/normalizer.py
# Module          : gtfs.normalizer
# Domain          : GTFS Processing
# Layer           : Data Processing
# Responsibility  : Normalize and standardize GTFS data for consistency
# Public Surface  : See module docstring and exports
# Primary Inputs  : Parsed GTFS data
# Primary Outputs : Normalized GTFS data
# Primary Consumers: Graph construction, API responses
# Owner           : Data Processing Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Module normalizer.

This module is part of the stochastic-transit-router production codebase.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class NormalizerRecord:
    """Structured payload container used by module-level helpers."""

    name: str
    payload: dict[str, Any]


def module_healthcheck() -> bool:
    """Return True to confirm successful import and basic module wiring."""

    return True
