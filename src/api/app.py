# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\app.py
# Module          : api.app
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of app
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""FastAPI application factory."""

from __future__ import annotations

from fastapi import FastAPI

from src.api.routers.benchmarks import router as benchmarks_router
from src.api.routers.datasets import router as datasets_router
from src.api.routers.disruption import router as disruption_router
from src.api.routers.experiments import router as experiments_router
from src.api.routers.feeds import router as feeds_router
from src.api.routers.graph import router as graph_router
from src.api.routers.health import router as health_router
from src.api.routers.reliability import router as reliability_router
from src.api.routers.routes import router as routes_router
from src.api.routers.topk import router as topk_router


app = FastAPI(title="stochastic-transit-router", version="0.1.0")
app.include_router(health_router)
app.include_router(feeds_router)
app.include_router(graph_router)
app.include_router(routes_router)
app.include_router(topk_router)
app.include_router(reliability_router)
app.include_router(disruption_router)
app.include_router(benchmarks_router)
app.include_router(experiments_router)
app.include_router(datasets_router)
