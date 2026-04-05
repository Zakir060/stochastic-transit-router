# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\algorithms\test_stochastic_shortest_path.py
# Module          : unit.algorithms.test_stochastic_shortest_path
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for stochastic_shortest_path module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for stochastic shortest path approximation."""

from __future__ import annotations

from src.algorithms.stochastic_shortest_path import stochastic_shortest_path
from src.graph.core import DirectedGraph


def test_stochastic_shortest_path_returns_expected_cost() -> None:
    graph = DirectedGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("e1", "A", "B", 7)
    result = stochastic_shortest_path(graph, "A", "B")
    assert result.expected_cost == 7
