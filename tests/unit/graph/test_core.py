# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\graph\test_core.py
# Module          : unit.graph.test_core
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for core module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for DirectedGraph."""

from __future__ import annotations

from src.graph.core import DirectedGraph


def test_graph_add_nodes_edges_and_status() -> None:
    graph = DirectedGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("e1", "A", "B", 5.0)
    status = graph.status()
    assert status.node_count == 2
    assert status.edge_count == 1


def test_graph_reversed_preserves_structure() -> None:
    graph = DirectedGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("e1", "A", "B", 3.0)
    rev = graph.reversed()
    edges = rev.neighbors("B")
    assert len(edges) == 1
    assert edges[0].to_node == "A"
