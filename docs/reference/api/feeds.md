# API Reference: Feeds

| Field | Value |
|---|---|
| Owner | Backend Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

The feeds endpoints expose a coarse, operator-facing view of dataset availability. This is intended to support service readiness checks and dashboards.

## Endpoint

- Method: `GET`
- Path: `/feeds/status`
- Authentication: none

## Response

Status: `200 OK`

```json
{
	"mta_gtfs": {"available": true, "freshness_seconds": 0},
	"mta_realtime": {"available": false, "reason": "endpoint not configured"},
	"tlc": {"available": true, "refresh": "monthly"},
	"osm": {"available": true, "refresh": "on_demand"}
}
```

### Semantics

- `available` is a boolean flag indicating whether the service considers the feed usable.
- `freshness_seconds` is a numeric age metric in seconds when present.
- `reason` is a human-readable explanation when a feed is unavailable.
- `refresh` documents the expected cadence (for example, `monthly`).

## Current limitations

This endpoint currently returns a static dictionary from the handler implementation and is not yet wired to the ingest manifests or freshness reports under `data/`.

If you need a real freshness computation, use the offline report generator:

```powershell
python scripts/check_feed_freshness.py
```

The script writes a machine-readable report to `data/cache/feed_freshness_report.json` and a CSV export to `data/exports/feed_freshness_report.csv`.

## Implementation

- Router: [src/api/routers/feeds.py](/src/api/routers/feeds.py)
- Handler: `feeds_status()`

## Related

- [Documentation Index](/docs/index.md)
- [API OpenAPI Spec](/docs/api/openapi.yaml)
- [Data Refresh](/docs/operations/data_refresh.md)
- [Feed Freshness Script](/scripts/check_feed_freshness.py)

---

Document Control

- Owner: API Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
