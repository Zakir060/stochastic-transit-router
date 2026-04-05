# API Reference: Routes

| Field | Value |
|---|---|
| Owner | Backend Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

The routes endpoint computes one or more candidate paths between a `source` node and a `destination` node under a selected objective (fastest, reliability-aware ranking, robust mean-variance scoring, or CVaR selection).

## Endpoint

- Method: `POST`
- Path: `/routes`
- Authentication: none

## Request body

The request uses the `RouteRequest` schema.

```json
{
	"source": "A",
	"destination": "D",
	"departure_time": "2026-04-05T12:00:00Z",
	"objective": "fastest"
}
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | yes | Graph node identifier. |
| `destination` | string | yes | Graph node identifier. |
| `departure_time` | string | yes | ISO-8601 timestamp string. Accepted for contract stability; not currently used by the handler logic. |
| `objective` | string | yes | One of `fastest`, `reliable`, `robust`, `cvar`. |
| `tau` | integer | no | Reliability horizon in seconds (only used when `objective=reliable`). Default: `3600`. |
| `lambda` | number | no | Risk aversion coefficient (only used when `objective=robust`). Default: `1.0`. |
| `alpha` | number | no | Tail probability level (only used when `objective=cvar`). Default: `0.95`. |

## Response

Status: `200 OK`

```json
{
	"objective": "fastest",
	"paths": [
		{
			"nodes": ["A", "B", "C", "D"],
			"cost": 14.0,
			"expected_cost": 14.0,
			"variance": 0.0,
			"reliability": null,
			"cvar": null
		}
	]
}
```

### Path metrics

| Field | Type | Description |
| --- | --- | --- |
| `nodes` | array[string] | Ordered node ids along the path. |
| `cost` | number | Objective-specific scalar used for ranking. For `fastest`, this is the deterministic shortest-path cost. For `robust`, this becomes a mean-variance score. |
| `expected_cost` | number or null | Expected cost estimate when available. Currently equal to `cost` for deterministic and expected-cost approximations. |
| `variance` | number or null | Variance estimate when available. Currently `0.0` for the stochastic approximation path. |
| `reliability` | number or null | Empirical probability estimate $P(T \\le \\tau)$ when `objective=reliable`. |
| `cvar` | number or null | Empirical CVaR estimate when `objective=cvar`. |

## Objective mapping

- `fastest`: deterministic Dijkstra shortest path.
- `reliable`: computes two candidates (deterministic and expected-cost approximation) and ranks them by reliability under a small, deterministic sample set.
- `robust`: ranks candidates by mean-variance score $\\mu + \\lambda\\sigma^2$ with a configurable $\\lambda$.
- `cvar`: selects the candidate with minimum CVaR at level $\\alpha$ under a small, deterministic sample set.

## Constraints and failure modes

- Node identifiers must exist in the in-memory graph loaded by the service. In the current development wiring, the graph is a small placeholder fixture (see implementation notes below).
- Invalid `objective` values are rejected by request validation (HTTP `422`).

## Implementation

- Router: [src/api/routers/routes.py](/src/api/routers/routes.py)
- Request/response schemas: [src/api/schemas.py](/src/api/schemas.py)
- Graph dependency (current placeholder graph): [src/api/deps.py](/src/api/deps.py)

## Related

- [API Reference: Top-k Routes](/docs/reference/api/topk.md)
- [Algorithm Reference: Dijkstra](/docs/reference/algorithms/dijkstra.md)
- [Algorithm Reference: Yen's $k$-Shortest Paths](/docs/reference/algorithms/yens.md)
- [Graph Model](/docs/math/graph_model.md)

---

Document Control

- Owner: API Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
