# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\routers\feeds.py
# Module          : api.routers.feeds
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of feeds
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Feed status endpoint router."""

from __future__ import annotations

from fastapi import APIRouter


router = APIRouter(prefix="/feeds", tags=["feeds"])


@router.get("/status")
def feeds_status() -> dict[str, object]:
    """Return feed availability summary."""

    return {
        "mta_gtfs": {"available": True, "freshness_seconds": 0},
        "mta_realtime": {"available": False, "reason": "endpoint not configured"},
        "tlc": {"available": True, "refresh": "monthly"},
        "osm": {"available": True, "refresh": "on_demand"},
    }
