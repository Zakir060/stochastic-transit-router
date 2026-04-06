from fastapi.testclient import TestClient

from src.api.app import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["version"] == "0.1.0"


def test_graph_status_endpoint() -> None:
    response = client.get("/graph/status")
    assert response.status_code == 200
    payload = response.json()
    assert payload["node_count"] == 4
    assert payload["edge_count"] == 5


def test_routes_endpoint_fastest() -> None:
    response = client.post(
        "/routes",
        json={
            "source": "A",
            "destination": "D",
            "departure_time": "2026-04-05T08:00:00Z",
            "objective": "fastest",
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["objective"] == "fastest"
    assert payload["paths"][0]["nodes"] == ["A", "B", "C", "D"]
    assert payload["paths"][0]["cost"] == 14.0
