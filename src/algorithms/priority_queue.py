# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\priority_queue.py
# Module          : algorithms.priority_queue
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of priority queue
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Priority queue abstraction over heapq."""

from __future__ import annotations

import heapq


class PriorityQueue:
    """Minimal priority queue with push and pop operations."""

    def __init__(self) -> None:
        self._heap: list[tuple[float, str]] = []

    def push(self, priority: float, node: str) -> None:
        """Insert node with priority."""

        heapq.heappush(self._heap, (priority, node))

    def pop(self) -> tuple[float, str]:
        """Pop smallest priority pair."""

        return heapq.heappop(self._heap)

    def __bool__(self) -> bool:
        """Return queue non-empty state."""

        return bool(self._heap)
