# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\integration\test_api_routes.py
# Module          : integration.test_api_routes
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for api_routes module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Integration tests for API routes."""

from __future__ import annotations

from fastapi.testclient import TestClient

from src.api.app import app


client = TestClient(app)


def test_health_endpoint_returns_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_routes_endpoint_returns_path() -> None:
    payload = {
        "source": "A",
        "destination": "D",
        "departure_time": "2026-04-05T08:00:00",
        "objective": "fastest",
    }
    response = client.post("/routes", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["paths"]
