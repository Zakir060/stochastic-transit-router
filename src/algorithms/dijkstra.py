# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\dijkstra.py
# Module          : algorithms.dijkstra
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of dijkstra
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Dijkstra shortest path algorithm.

Problem statement:
Find a minimum-cost path in a directed graph with non-negative edge weights.

Complexity:
Time O((|V| + |E|) log |V|) using a binary heap.
Space O(|V|) for distances and predecessor maps.

Reference:
E. W. Dijkstra, A note on two problems in connexion with graphs, 1959.

Limitations:
Edge weights must be non-negative. Negative edges violate optimality guarantees.
"""

from __future__ import annotations

import heapq
import math

from src.algorithms.path_utils import reconstruct_path
from src.graph.core import DirectedGraph
from src.models.path import PathResult


def dijkstra_shortest_path(graph: DirectedGraph, source: str, target: str) -> PathResult:
    """Compute shortest path between source and target using Dijkstra."""

    if not graph.has_node(source) or not graph.has_node(target):
        return PathResult(nodes=[], cost=math.inf)

    distance: dict[str, float] = {source: 0.0}
    predecessor: dict[str, str] = {}
    queue: list[tuple[float, str]] = [(0.0, source)]
    visited: set[str] = set()

    while queue:
        current_distance, node = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        if node == target:
            break
        for edge in graph.neighbors(node):
            if edge.weight < 0:
                raise ValueError("Dijkstra requires non-negative edge weights")
            candidate = current_distance + edge.weight
            if candidate < distance.get(edge.to_node, math.inf):
                distance[edge.to_node] = candidate
                predecessor[edge.to_node] = node
                heapq.heappush(queue, (candidate, edge.to_node))

    path = reconstruct_path(predecessor, source, target)
    if not path:
        return PathResult(nodes=[], cost=math.inf)

    edge_ids: list[str] = []
    for idx in range(len(path) - 1):
        from_node = path[idx]
        to_node = path[idx + 1]
        for edge in graph.neighbors(from_node):
            if edge.to_node == to_node:
                edge_ids.append(edge.edge_id)
                break

    return PathResult(nodes=path, cost=distance[target], edges=edge_ids, expected_cost=distance[target])


def _example_assertions() -> None:
    graph = DirectedGraph()
    for node in ("A", "B", "C"):
        graph.add_node(node)
    graph.add_edge("e1", "A", "B", 1.0)
    graph.add_edge("e2", "B", "C", 2.0)
    graph.add_edge("e3", "A", "C", 5.0)
    result = dijkstra_shortest_path(graph, "A", "C")
    assert result.nodes == ["A", "B", "C"]
    assert result.cost == 3.0


