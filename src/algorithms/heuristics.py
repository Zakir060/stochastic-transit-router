# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\heuristics.py
# Module          : algorithms.heuristics
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of heuristics
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Heuristic functions for informed graph search."""

from __future__ import annotations

import math

from src.graph.core import DirectedGraph


def haversine_distance_meters(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Return haversine distance in meters between two coordinates."""

    radius = 6371000.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * radius * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def temporal_haversine_heuristic(graph: DirectedGraph, node: str, destination: str, vmax_mps: float = 33.34) -> float:
    """Admissible A star heuristic based on distance over upper speed bound."""

    source_node = graph.node(node)
    destination_node = graph.node(destination)
    meters = haversine_distance_meters(source_node.lat, source_node.lon, destination_node.lat, destination_node.lon)
    return meters / vmax_mps
