# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\routers\routes.py
# Module          : api.routers.routes
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of routes
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Primary route query endpoint."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from src.algorithms.dijkstra import dijkstra_shortest_path
from src.algorithms.cvar_router import select_min_cvar_path
from src.algorithms.reliability_router import rank_by_reliability
from src.algorithms.robust_router import rank_by_robust_score
from src.algorithms.stochastic_shortest_path import stochastic_shortest_path
from src.api.deps import get_graph
from src.api.schemas import PathResponse, RouteRequest, RouteResponse
from src.models.path import PathResult


router = APIRouter(tags=["routes"])


def _as_response_path(path: PathResult) -> PathResponse:
    return PathResponse(
        nodes=path.nodes,
        cost=path.cost,
        expected_cost=path.expected_cost,
        variance=path.variance,
        reliability=path.reliability,
        cvar=path.cvar,
    )


@router.post("/routes", response_model=RouteResponse)
def route_query(payload: RouteRequest, graph=Depends(get_graph)) -> RouteResponse:
    """Compute route under selected objective."""

    base = dijkstra_shortest_path(graph, payload.source, payload.destination)
    stochastic = stochastic_shortest_path(graph, payload.source, payload.destination)
    candidates = [base, stochastic]

    objective = payload.objective
    if objective == "reliable":
        ranked = rank_by_reliability(candidates, payload.tau or 3600)
        return RouteResponse(objective=objective, paths=[_as_response_path(item) for item in ranked])
    if objective == "robust":
        ranked = rank_by_robust_score(candidates, payload.lambda_value or 1.0)
        return RouteResponse(objective=objective, paths=[_as_response_path(item) for item in ranked])
    if objective == "cvar":
        selected = select_min_cvar_path(candidates, payload.alpha or 0.95)
        return RouteResponse(objective=objective, paths=[_as_response_path(selected)] if selected else [])

    return RouteResponse(objective=objective, paths=[_as_response_path(base)])
