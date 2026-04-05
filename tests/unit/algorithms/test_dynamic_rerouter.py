# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\algorithms\test_dynamic_rerouter.py
# Module          : unit.algorithms.test_dynamic_rerouter
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for dynamic_rerouter module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for dynamic rerouting."""

from __future__ import annotations

from src.algorithms.dynamic_rerouter import reroute_with_delays
from src.graph.core import DirectedGraph


def test_dynamic_rerouter_applies_delay() -> None:
    graph = DirectedGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("e1", "A", "B", 5)
    result = reroute_with_delays(graph, "A", "B", {"e1": 3})
    assert result.cost == 8
