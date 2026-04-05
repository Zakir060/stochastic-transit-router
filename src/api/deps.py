# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\deps.py
# Module          : api.deps
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of deps
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Dependency providers for API routers."""

from __future__ import annotations

from src.graph.core import DirectedGraph


_GRAPH: DirectedGraph | None = None


def get_graph() -> DirectedGraph:
    """Return singleton in-memory graph used by API handlers."""

    global _GRAPH
    if _GRAPH is None:
        graph = DirectedGraph()
        for node in ("A", "B", "C", "D"):
            graph.add_node(node, lat=40.0, lon=-73.0)
        graph.add_edge("e1", "A", "B", 5)
        graph.add_edge("e2", "B", "C", 5)
        graph.add_edge("e3", "A", "C", 15)
        graph.add_edge("e4", "C", "D", 4)
        graph.add_edge("e5", "B", "D", 20)
        _GRAPH = graph
    return _GRAPH
