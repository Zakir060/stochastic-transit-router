# Data Refresh

| Field | Value |
|---|---|
| Owner | DevOps Team |
| Department | Documentation |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

This document defines refresh cadence and operational checks for all external data feeds used by stochastic-transit-router.

## Refresh table

| Source | Cadence | Method | Failure handling |
|:--|:--|:--|:--|
| MTA GTFS | daily | scheduled download | raise DataSourceUnavailableError |
| MTA GTFS RT | 30 seconds | polling | retry with bounded backoff |
| NYC TLC | monthly | official listing discovery | skip month if file unavailable |
| OSM Overpass | on demand | query by bounding box | respect fair use delay |

## Related

- [GTFS dataset](/docs/datasets/gtfs.md)
- [GTFS Realtime dataset](/docs/datasets/gtfs_realtime.md)
- [OSM Overpass dataset](/docs/datasets/osm_overpass.md)

---

Document Control

- Owner: Operations Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
