# API Reference: Health

| Field | Value |
|---|---|
| Owner | Backend Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

The health endpoint provides a lightweight liveness signal for process monitoring and local development. It is intentionally free of external I/O so that failures in upstream data sources do not affect basic service health reporting.

## Endpoint

- Method: `GET`
- Path: `/health`
- Authentication: none

## Response

Status: `200 OK`

```json
{
	"status": "ok",
	"version": "0.1.0",
	"uptime_seconds": 12.345
}
```

### Fields

| Field | Type | Description |
| --- | --- | --- |
| `status` | string | Constant value `ok` when the process is running and able to respond. |
| `version` | string | Service version string currently hard-coded in the handler. |
| `uptime_seconds` | number | Seconds since process start (monotonic wall-clock delta). |

## Operational notes

- This endpoint is a liveness signal, not a full readiness check. It does not verify that datasets are present, fresh, or parseable.
- For a (currently minimal) feed availability summary, see `/feeds/status`.

## Implementation

- Router: [src/api/routers/health.py](/src/api/routers/health.py)
- Handler: `health()`

## Related

- [Documentation Index](/docs/index.md)
- [API OpenAPI Spec](/docs/api/openapi.yaml)
- [Architecture Overview](/docs/architecture/overview.md)

---

Document Control

- Owner: API Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
