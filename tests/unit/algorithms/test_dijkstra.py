# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\algorithms\test_dijkstra.py
# Module          : unit.algorithms.test_dijkstra
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for dijkstra module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for Dijkstra algorithm."""

from __future__ import annotations

from src.algorithms.dijkstra import dijkstra_shortest_path
from src.graph.core import DirectedGraph


def test_dijkstra_shortest_path_cost_and_nodes() -> None:
    graph = DirectedGraph()
    for node in ("A", "B", "C"):
        graph.add_node(node)
    graph.add_edge("e1", "A", "B", 1)
    graph.add_edge("e2", "B", "C", 2)
    graph.add_edge("e3", "A", "C", 5)

    result = dijkstra_shortest_path(graph, "A", "C")
    assert result.nodes == ["A", "B", "C"]
    assert result.cost == 3


def test_dijkstra_unreachable_returns_infinite_cost() -> None:
    graph = DirectedGraph()
    graph.add_node("A")
    graph.add_node("B")
    result = dijkstra_shortest_path(graph, "A", "B")
    assert result.nodes == []
    assert result.cost == float("inf")
