# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\algorithms\test_astar.py
# Module          : unit.algorithms.test_astar
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for astar module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for A star routing."""

from __future__ import annotations

from src.algorithms.astar import astar_shortest_path
from src.graph.core import DirectedGraph


def test_astar_finds_short_path() -> None:
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
