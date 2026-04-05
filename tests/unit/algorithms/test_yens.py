# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\algorithms\test_yens.py
# Module          : unit.algorithms.test_yens
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for yens module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for Yen top-k paths."""

from __future__ import annotations

from src.algorithms.yens import yens_k_shortest_paths
from src.graph.core import DirectedGraph


def test_yens_returns_ordered_paths() -> None:
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
