# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\time_dependent.py
# Module          : algorithms.time_dependent
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of time dependent
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Time-dependent shortest path search.

Complexity:
Time O((|V| + |E|) log |V|) with time-dependent edge evaluation.
Space O(|V|).
"""

from __future__ import annotations

import heapq
import math
from typing import Callable

from src.algorithms.path_utils import reconstruct_path
from src.graph.core import DirectedGraph
from src.graph.edge import Edge
from src.models.path import PathResult


WeightFunction = Callable[[Edge, int], float]


def time_dependent_shortest_path(
    graph: DirectedGraph,
    source: str,
    target: str,
    departure_time: int,
    weight_function: WeightFunction | None = None,
) -> PathResult:
    """Compute shortest path with departure-time dependent edge costs."""

    if not graph.has_node(source) or not graph.has_node(target):
        return PathResult(nodes=[], cost=math.inf)

    dist: dict[str, float] = {source: 0.0}
    prev: dict[str, str] = {}
    queue: list[tuple[float, str, int]] = [(0.0, source, departure_time)]

    while queue:
        current_cost, node, current_time = heapq.heappop(queue)
        if node == target:
            break
        for edge in graph.neighbors(node):
            edge_cost = edge.weight if weight_function is None else weight_function(edge, current_time)
            candidate = current_cost + edge_cost
            if candidate < dist.get(edge.to_node, math.inf):
                dist[edge.to_node] = candidate
                prev[edge.to_node] = node
                heapq.heappush(queue, (candidate, edge.to_node, current_time + int(edge_cost)))

    path = reconstruct_path(prev, source, target)
    if not path:
        return PathResult(nodes=[], cost=math.inf)
    return PathResult(nodes=path, cost=dist[target], expected_cost=dist[target])
