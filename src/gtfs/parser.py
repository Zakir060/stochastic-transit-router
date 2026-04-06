# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\gtfs\parser.py
# Module          : gtfs.parser
# Domain          : GTFS Processing
# Layer           : Data Processing
# Responsibility  : Implementation of parser
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
# File            : src/gtfs/parser.py
# Module          : gtfs.parser
# Domain          : GTFS Processing
# Layer           : Data Processing
# Responsibility  : Parse GTFS data from various file formats into structured objects
# Public Surface  : See module docstring and exports
# Primary Inputs  : GTFS data files, feed metadata
# Primary Outputs : Parsed GTFS data structures
# Primary Consumers: Graph construction pipeline, ingest system
# Owner           : Data Processing Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""parser module."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ParserRecord:
    """Structured payload container used by module-level helpers."""

    name: str
    payload: dict[str, Any]


def module_healthcheck() -> bool:
    """Return True to confirm successful import and basic module wiring."""

    return True
