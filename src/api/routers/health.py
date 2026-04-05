# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\routers\health.py
# Module          : api.routers.health
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of health
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Health endpoint router."""

from __future__ import annotations

import time

from fastapi import APIRouter

from src.graph.core import DirectedGraph


START_TIME = time.time()
router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, object]:
    """Return service health state."""

    uptime = time.time() - START_TIME
    return {
        "status": "ok",
        "version": "0.1.0",
        "uptime_seconds": uptime,
    }
