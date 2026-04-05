# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\bidirectional_dijkstra.py
# Module          : algorithms.bidirectional_dijkstra
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of bidirectional dijkstra
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Bidirectional Dijkstra shortest path algorithm.

Complexity:
Time O((|V| + |E|) log |V|) with practical speedup from dual search fronts.
Space O(|V|).
"""

from __future__ import annotations

import heapq
import math

from src.graph.core import DirectedGraph
from src.models.path import PathResult


def bidirectional_dijkstra(graph: DirectedGraph, source: str, target: str) -> PathResult:
    """Run bidirectional shortest path search."""

    if not graph.has_node(source) or not graph.has_node(target):
        return PathResult(nodes=[], cost=math.inf)

    reverse = graph.reversed()
    dist_f: dict[str, float] = {source: 0.0}
    dist_b: dict[str, float] = {target: 0.0}
    prev_f: dict[str, str] = {}
    prev_b: dict[str, str] = {}
    pq_f: list[tuple[float, str]] = [(0.0, source)]
    pq_b: list[tuple[float, str]] = [(0.0, target)]
    seen_f: set[str] = set()
    seen_b: set[str] = set()
    best = math.inf
    meeting: str | None = None

    while pq_f and pq_b:
        df, node_f = heapq.heappop(pq_f)
        if node_f not in seen_f:
            seen_f.add(node_f)
            if node_f in seen_b and df + dist_b[node_f] < best:
                best = df + dist_b[node_f]
                meeting = node_f
            for edge in graph.neighbors(node_f):
                cand = df + edge.weight
                if cand < dist_f.get(edge.to_node, math.inf):
                    dist_f[edge.to_node] = cand
                    prev_f[edge.to_node] = node_f
                    heapq.heappush(pq_f, (cand, edge.to_node))

        db, node_b = heapq.heappop(pq_b)
        if node_b not in seen_b:
            seen_b.add(node_b)
            if node_b in seen_f and db + dist_f[node_b] < best:
                best = db + dist_f[node_b]
                meeting = node_b
            for edge in reverse.neighbors(node_b):
                cand = db + edge.weight
                if cand < dist_b.get(edge.to_node, math.inf):
                    dist_b[edge.to_node] = cand
                    prev_b[edge.to_node] = node_b
                    heapq.heappush(pq_b, (cand, edge.to_node))

    if meeting is None:
        return PathResult(nodes=[], cost=math.inf)

    front: list[str] = []
    current = meeting
    while current != source:
        front.append(current)
        current = prev_f[current]
    front.append(source)
    front.reverse()

    back: list[str] = []
    current = meeting
    while current != target:
        current = prev_b[current]
        back.append(current)

    return PathResult(nodes=front + back, cost=best, expected_cost=best)
