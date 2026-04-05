# API Reference: Top-k Routes

| Field | Value |
|---|---|
| Owner | Backend Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

The top-k endpoint returns up to $k$ loopless candidate paths between `source` and `destination` using Yen's algorithm.

## Endpoint

- Method: `POST`
- Path: `/routes/topk`
- Authentication: none

## Request body

The request uses the `TopKRequest` schema.

```json
{
	"source": "A",
	"destination": "D",
	"departure_time": "2026-04-05T12:00:00Z",
	"objective": "fastest",
	"k": 3
}
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | yes | Graph node identifier. |
| `destination` | string | yes | Graph node identifier. |
| `departure_time` | string | yes | ISO-8601 timestamp string. Accepted for contract stability; not currently used by the handler logic. |
| `objective` | string | yes | One of `fastest`, `reliable`, `robust`, `cvar`. Currently returned verbatim in the response but not used to change the algorithm. |
| `k` | integer | yes | Maximum number of paths to return. Range: 1–20. |

## Response

Status: `200 OK`

```json
{
	"objective": "fastest",
	"paths": [
		{"nodes": ["A", "B", "C", "D"], "cost": 14.0},
		{"nodes": ["A", "C", "D"], "cost": 19.0}
	]
}
```

## Implementation

- Router: [src/api/routers/topk.py](/src/api/routers/topk.py)
- Algorithm: [src/algorithms/yens.py](/src/algorithms/yens.py)
- Request/response schemas: [src/api/schemas.py](/src/api/schemas.py)

## Related

- [API Reference: Routes](/docs/reference/api/routes.md)
- [Algorithm Reference: Yen's $k$-Shortest Paths](/docs/reference/algorithms/yens.md)
- [Graph Model](/docs/math/graph_model.md)

---

Document Control

- Owner: API Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
