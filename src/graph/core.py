# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\graph\core.py
# Module          : graph.core
# Domain          : Graph
# Layer           : Data Structure
# Responsibility  : Implementation of core
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing algorithms, API
# Owner           : Graph Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Core adjacency graph implementation for routing algorithms."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable

from src.graph.edge import Edge
from src.graph.node import Node


@dataclass(slots=True)
class GraphStatus:
    """Structural summary for observability endpoints."""

    node_count: int
    edge_count: int


class DirectedGraph:
    """Directed weighted graph with typed nodes and edges."""

    def __init__(self) -> None:
        self._nodes: dict[str, Node] = {}
        self._adjacency: dict[str, list[Edge]] = defaultdict(list)
        self._edge_index: dict[str, Edge] = {}

    def add_node(
        self,
        node_id: str,
        node_type: str = "transit_stop",
        lat: float = 0.0,
        lon: float = 0.0,
        metadata: dict[str, str] | None = None,
    ) -> None:
        """Insert or replace a node."""

        self._nodes[node_id] = Node(node_id=node_id, node_type=node_type, lat=lat, lon=lon, metadata=metadata or {})

    def add_edge(
        self,
        edge_id: str,
        from_node: str,
        to_node: str,
        weight: float,
        edge_type: str = "scheduled_movement",
        metadata: dict[str, float] | None = None,
    ) -> None:
        """Insert or replace a directed edge."""

        if from_node not in self._nodes:
            self.add_node(from_node)
        if to_node not in self._nodes:
            self.add_node(to_node)
        edge = Edge(edge_id=edge_id, from_node=from_node, to_node=to_node, weight=weight, edge_type=edge_type, metadata=metadata or {})
        self._adjacency[from_node] = [candidate for candidate in self._adjacency[from_node] if candidate.edge_id != edge_id]
        self._adjacency[from_node].append(edge)
        self._edge_index[edge_id] = edge

    def update_edge_weight(self, edge_id: str, weight: float) -> None:
        """Update a specific edge weight in place."""

        edge = self._edge_index[edge_id]
        edge.weight = weight

    def neighbors(self, node_id: str) -> list[Edge]:
        """Return outgoing edges from node."""

        return list(self._adjacency.get(node_id, []))

    def nodes(self) -> Iterable[str]:
        """Return node ids."""

        return self._nodes.keys()

    def edges(self) -> Iterable[Edge]:
        """Return all edges."""

        return self._edge_index.values()

    def node(self, node_id: str) -> Node:
        """Return node by id."""

        return self._nodes[node_id]

    def has_node(self, node_id: str) -> bool:
        """Return node existence."""

        return node_id in self._nodes

    def status(self) -> GraphStatus:
        """Return graph status snapshot."""

        return GraphStatus(node_count=len(self._nodes), edge_count=len(self._edge_index))

    def reversed(self) -> DirectedGraph:
        """Return graph with all edges reversed."""

        other = DirectedGraph()
        for node in self._nodes.values():
            other.add_node(node.node_id, node.node_type, node.lat, node.lon, dict(node.metadata))
        for edge in self._edge_index.values():
            other.add_edge(edge.edge_id, edge.to_node, edge.from_node, edge.weight, edge.edge_type, dict(edge.metadata))
        return other
