# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\graph\edge.py
# Module          : graph.edge
# Domain          : Graph
# Layer           : Data Structure
# Responsibility  : Implementation of edge
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing algorithms, API
# Owner           : Graph Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Graph edge model."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Edge:
    """Directed weighted edge in transit graph."""

    edge_id: str
    from_node: str
    to_node: str
    weight: float
    edge_type: str = "scheduled_movement"
    metadata: dict[str, float] = field(default_factory=dict)
