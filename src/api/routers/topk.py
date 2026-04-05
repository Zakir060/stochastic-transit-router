# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\routers\topk.py
# Module          : api.routers.topk
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of topk
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Top-k route endpoint."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from src.algorithms.yens import yens_k_shortest_paths
from src.api.deps import get_graph
from src.api.schemas import PathResponse, RouteResponse, TopKRequest


router = APIRouter(prefix="/routes", tags=["routes"])


@router.post("/topk", response_model=RouteResponse)
def topk_query(payload: TopKRequest, graph=Depends(get_graph)) -> RouteResponse:
    """Compute top-k loopless paths."""

    paths = yens_k_shortest_paths(graph, payload.source, payload.destination, payload.k)
    mapped = [
        PathResponse(
            nodes=item.nodes,
            cost=item.cost,
            expected_cost=item.expected_cost,
            variance=item.variance,
            reliability=item.reliability,
            cvar=item.cvar,
        )
        for item in paths
    ]
    return RouteResponse(objective=payload.objective, paths=mapped)
