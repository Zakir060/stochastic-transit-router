# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\routers\reliability.py
# Module          : api.routers.reliability
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of reliability
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Reliability endpoint."""

from __future__ import annotations

from fastapi import APIRouter, Query


router = APIRouter(prefix="/routes", tags=["routes"])


@router.get("/reliability")
def route_reliability(tau: int = Query(3600, ge=1)) -> dict[str, object]:
    """Return route reliability score payload."""

    return {
        "tau": tau,
        "reliability": 0.75,
        "confidence_interval": [0.70, 0.80],
    }
