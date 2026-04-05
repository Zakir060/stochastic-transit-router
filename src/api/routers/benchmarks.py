# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\routers\benchmarks.py
# Module          : api.routers.benchmarks
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of benchmarks
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Benchmark status endpoint."""

from __future__ import annotations

from fastapi import APIRouter


router = APIRouter(prefix="/benchmarks", tags=["benchmarks"])


@router.get("/status")
def benchmark_status() -> dict[str, object]:
    """Return benchmark status summary."""

    return {"status": "not_started", "last_run": None}
