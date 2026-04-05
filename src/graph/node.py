# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\graph\node.py
# Module          : graph.node
# Domain          : Graph
# Layer           : Data Structure
# Responsibility  : Implementation of node
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing algorithms, API
# Owner           : Graph Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Graph node model."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Node:
    """Typed transit graph node."""

    node_id: str
    node_type: str
    lat: float
    lon: float
    metadata: dict[str, str] = field(default_factory=dict)
