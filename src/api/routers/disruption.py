# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\routers\disruption.py
# Module          : api.routers.disruption
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of disruption
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Disruption endpoint."""

from __future__ import annotations

from fastapi import APIRouter


router = APIRouter(tags=["disruption"])


@router.get("/disruptions")
def disruptions() -> dict[str, object]:
    """Return active disruptions list."""

    return {"active": []}
