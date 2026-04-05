# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\astar.py
# Module          : algorithms.astar
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of astar
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""A star shortest path algorithm with admissible haversine heuristic.

Complexity:
Time O((|V| + |E|) log |V|) in typical sparse graphs.
Space O(|V|) for frontier and predecessor maps.
"""

from __future__ import annotations

import heapq
import math

from src.algorithms.heuristics import temporal_haversine_heuristic
from src.algorithms.path_utils import reconstruct_path
from src.graph.core import DirectedGraph
from src.models.path import PathResult


def astar_shortest_path(graph: DirectedGraph, source: str, target: str) -> PathResult:
    """Compute shortest path using A star heuristic search."""

    if not graph.has_node(source) or not graph.has_node(target):
        return PathResult(nodes=[], cost=math.inf)

    g_score: dict[str, float] = {source: 0.0}
    predecessor: dict[str, str] = {}
    open_set: list[tuple[float, str]] = [(0.0, source)]
    closed: set[str] = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        if current in closed:
            continue
        if current == target:
            break
        closed.add(current)

        for edge in graph.neighbors(current):
            tentative = g_score[current] + edge.weight
            if tentative < g_score.get(edge.to_node, math.inf):
                predecessor[edge.to_node] = current
                g_score[edge.to_node] = tentative
                h_value = temporal_haversine_heuristic(graph, edge.to_node, target)
                heapq.heappush(open_set, (tentative + h_value, edge.to_node))

    path = reconstruct_path(predecessor, source, target)
    if not path:
        return PathResult(nodes=[], cost=math.inf)
    return PathResult(nodes=path, cost=g_score[target], expected_cost=g_score[target])


def _example_assertions() -> None:
    graph = DirectedGraph()
    graph.add_node("A", lat=40.0, lon=-73.0)
    graph.add_node("B", lat=40.0005, lon=-73.0005)
    graph.add_node("C", lat=40.001, lon=-73.001)
    graph.add_edge("e1", "A", "B", 1.0)
    graph.add_edge("e2", "B", "C", 1.0)
    graph.add_edge("e3", "A", "C", 5.0)
    result = astar_shortest_path(graph, "A", "C")
    assert result.nodes == ["A", "B", "C"]
    assert result.cost == 2.0


_example_assertions()
