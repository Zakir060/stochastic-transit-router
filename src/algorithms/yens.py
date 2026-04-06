# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\yens.py
# Module          : algorithms.yens
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of yens
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Yen k-shortest loopless paths algorithm.

Complexity:
O(k * n * (m + n log n)) when Dijkstra is used as the subroutine.
"""

from __future__ import annotations

import copy
import math

from src.algorithms.dijkstra import dijkstra_shortest_path
from src.graph.core import DirectedGraph
from src.models.path import PathResult


def _path_cost(graph: DirectedGraph, nodes: list[str]) -> float:
    cost = 0.0
    for idx in range(len(nodes) - 1):
        from_node = nodes[idx]
        to_node = nodes[idx + 1]
        for edge in graph.neighbors(from_node):
            if edge.to_node == to_node:
                cost += edge.weight
                break
    return cost


def yens_k_shortest_paths(graph: DirectedGraph, source: str, target: str, k: int) -> list[PathResult]:
    """Return up to k loopless shortest paths ordered by cost."""

    if k <= 0:
        return []

    first = dijkstra_shortest_path(graph, source, target)
    if not first.nodes:
        return []

    shortest: list[PathResult] = [first]
    candidates: list[PathResult] = []

    for kth in range(1, k):
        previous = shortest[kth - 1].nodes
        for idx in range(len(previous) - 1):
            spur_node = previous[idx]
            root_path = previous[: idx + 1]

            temp_graph = copy.deepcopy(graph)
            for path in shortest:
                if len(path.nodes) > idx and path.nodes[: idx + 1] == root_path:
                    from_node = path.nodes[idx]
                    to_node = path.nodes[idx + 1]
                    temp_graph._adjacency[from_node] = [
                        edge for edge in temp_graph.neighbors(from_node) if edge.to_node != to_node
                    ]

            spur_path = dijkstra_shortest_path(temp_graph, spur_node, target)
            if not spur_path.nodes:
                continue
            total_nodes = root_path[:-1] + spur_path.nodes
            total_cost = _path_cost(graph, total_nodes)
            candidate = PathResult(nodes=total_nodes, cost=total_cost, expected_cost=total_cost)
            if candidate.nodes not in [item.nodes for item in candidates] and candidate.nodes not in [item.nodes for item in shortest]:
                candidates.append(candidate)

        if not candidates:
            break
        candidates.sort(key=lambda item: item.cost)
        shortest.append(candidates.pop(0))

    return shortest


def _example_assertions() -> None:
    graph = DirectedGraph()
    for node in ("A", "B", "C", "D"):
        graph.add_node(node)
    graph.add_edge("e1", "A", "B", 1)
    graph.add_edge("e2", "B", "D", 1)
    graph.add_edge("e3", "A", "C", 1)
    graph.add_edge("e4", "C", "D", 1)
    graph.add_edge("e5", "A", "D", 3)
    paths = yens_k_shortest_paths(graph, "A", "D", 3)
    assert len(paths) >= 2
    assert paths[0].cost <= paths[1].cost


