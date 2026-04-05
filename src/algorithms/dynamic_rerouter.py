# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\dynamic_rerouter.py
# Module          : algorithms.dynamic_rerouter
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of dynamic rerouter
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Realtime delay injection and rerouting."""

from __future__ import annotations

from src.algorithms.dijkstra import dijkstra_shortest_path
from src.graph.core import DirectedGraph
from src.models.path import PathResult


def reroute_with_delays(
    graph: DirectedGraph,
    source: str,
    target: str,
    delays_by_edge_id: dict[str, float],
) -> PathResult:
    """Apply delay deltas to graph edges and recompute shortest path."""

    for edge in graph.edges():
        if edge.edge_id in delays_by_edge_id:
            edge.weight += delays_by_edge_id[edge.edge_id]
    return dijkstra_shortest_path(graph, source, target)
