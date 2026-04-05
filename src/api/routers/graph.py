# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\routers\graph.py
# Module          : api.routers.graph
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of graph
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Graph status endpoint router."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from src.api.deps import get_graph


router = APIRouter(prefix="/graph", tags=["graph"])


@router.get("/status")
def graph_status(graph=Depends(get_graph)) -> dict[str, object]:
    """Return in-memory graph status summary."""

    status = graph.status()
    return {
        "node_count": status.node_count,
        "edge_count": status.edge_count,
        "last_build_timestamp": "not_built_from_external_data",
        "config_hash": "phase1-bootstrap",
    }
