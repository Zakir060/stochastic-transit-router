# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\schemas.py
# Module          : api.schemas
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of schemas
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Pydantic request and response schemas for API endpoints."""

from __future__ import annotations

from pydantic import BaseModel, Field


class RouteRequest(BaseModel):
    """Route query payload."""

    source: str
    destination: str
    departure_time: str
    objective: str = Field(pattern="^(fastest|reliable|robust|cvar)$")
    lambda_value: float | None = Field(default=None, alias="lambda")
    tau: int | None = None
    alpha: float | None = None


class TopKRequest(RouteRequest):
    """Top-k route request payload."""

    k: int = Field(ge=1, le=20)


class PathResponse(BaseModel):
    """Path metrics payload."""

    nodes: list[str]
    cost: float
    expected_cost: float | None = None
    variance: float | None = None
    reliability: float | None = None
    cvar: float | None = None


class RouteResponse(BaseModel):
    """Route response payload."""

    objective: str
    paths: list[PathResponse]
