# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\algorithms\test_bidirectional_dijkstra.py
# Module          : unit.algorithms.test_bidirectional_dijkstra
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for bidirectional_dijkstra module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for bidirectional Dijkstra."""

from __future__ import annotations

from src.algorithms.bidirectional_dijkstra import bidirectional_dijkstra
from src.graph.core import DirectedGraph


def test_bidirectional_matches_expected_cost() -> None:
    graph = DirectedGraph()
    for node in ("A", "B", "C", "D"):
        graph.add_node(node)
    graph.add_edge("e1", "A", "B", 1)
    graph.add_edge("e2", "B", "D", 1)
    graph.add_edge("e3", "A", "C", 1)
    graph.add_edge("e4", "C", "D", 2)
    result = bidirectional_dijkstra(graph, "A", "D")
    assert result.cost == 2
    assert result.nodes[0] == "A"
    assert result.nodes[-1] == "D"
