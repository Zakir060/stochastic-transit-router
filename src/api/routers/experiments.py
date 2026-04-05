# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\routers\experiments.py
# Module          : api.routers.experiments
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of experiments
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Experiment metadata endpoint."""

from __future__ import annotations

from fastapi import APIRouter


router = APIRouter(prefix="/experiments", tags=["experiments"])


@router.get("/metadata")
def experiments_metadata() -> dict[str, object]:
    """Return experiment index metadata."""

    return {
        "experiments": [
            {"id": "exp_001", "status": "experiment not yet executed"},
            {"id": "exp_002", "status": "experiment not yet executed"},
        ]
    }
