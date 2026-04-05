# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\stochastic_shortest_path.py
# Module          : algorithms.stochastic_shortest_path
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of stochastic shortest path
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Stochastic shortest path approximation using expected edge costs."""

from __future__ import annotations

from src.algorithms.dijkstra import dijkstra_shortest_path
from src.graph.core import DirectedGraph
from src.models.path import PathResult


def stochastic_shortest_path(graph: DirectedGraph, source: str, target: str) -> PathResult:
    """Approximate stochastic shortest path by minimizing expected edge costs."""

    path = dijkstra_shortest_path(graph, source, target)
    path.expected_cost = path.cost
    path.variance = 0.0
    return path
