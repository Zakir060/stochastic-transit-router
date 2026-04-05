# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\osm\overpass_client.py
# Module          : osm.overpass_client
# Domain          : OSM Processing
# Layer           : Data Processing
# Responsibility  : Implementation of overpass client
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Graph construction
# Owner           : Data Processing Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src/osm/overpass_client.py
# Module          : osm.overpass_client
# Domain          : OSM Processing
# Layer           : Data Processing
# Responsibility  : Query OpenStreetMap data via Overpass API
# Public Surface  : Overpass API client interfaces
# Primary Inputs  : OSM queries and bounding boxes
# Primary Outputs : Raw OSM data from Overpass
# Primary Consumers: OSM parser, graph construction
# Owner           : Data Processing Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Module overpass_client.

This module is part of the stochastic-transit-router production codebase.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class OverpassClientRecord:
    """Structured payload container used by module-level helpers."""

    name: str
    payload: dict[str, Any]


def module_healthcheck() -> bool:
    """Return True to confirm successful import and basic module wiring."""

    return True
