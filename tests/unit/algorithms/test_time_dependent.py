# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\algorithms\test_time_dependent.py
# Module          : unit.algorithms.test_time_dependent
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for time_dependent module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for time-dependent routing."""

from __future__ import annotations

from src.algorithms.time_dependent import time_dependent_shortest_path
from src.graph.core import DirectedGraph


def test_time_dependent_uses_weight_function() -> None:
    graph = DirectedGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("e1", "A", "B", 10)

    def dynamic_weight(_, departure_time: int) -> float:
        return 5 if departure_time < 100 else 20

    early = time_dependent_shortest_path(graph, "A", "B", 50, dynamic_weight)
    late = time_dependent_shortest_path(graph, "A", "B", 150, dynamic_weight)
    assert early.cost == 5
    assert late.cost == 20
