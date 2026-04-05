# GTFS Realtime Dataset

| Field | Value |
|---|---|
| Owner | Data Engineering |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This document describes realtime feed entities, static mapping strategy, and polling control parameters.

## Entity types

| Entity | Proto message | Key fields | Mapping to static GTFS | Update action |
|:--|:--|:--|:--|:--|
| TripUpdate | FeedEntity.trip_update | trip_id route_id stop_time_update delay | trip_id to trips.trip_id | edge delay update |
| VehiclePosition | FeedEntity.vehicle | trip_id vehicle_id position timestamp | trip_id and stop sequence context | optional telemetry update |
| ServiceAlert | FeedEntity.alert | informed_entity effect severity active_period | route_id trip_id or stop_id mapping | disruption penalty update |

## Polling strategy parameters

| Parameter | Default | Description | Config key |
|:--|:--|:--|:--|
| interval seconds | 30 | pull period for each feed endpoint | configs/feeds/mta_realtime.yaml polling.interval_seconds |
| timeout seconds | 15 | request timeout per poll | configs/feeds/mta_realtime.yaml polling.timeout_seconds |
| max failures | 10 | threshold before source unavailable status | configs/feeds/mta_realtime.yaml polling.max_consecutive_failures |
| stale threshold | 180 | age threshold to mark feed stale | configs/default.yaml realtime.stale_feed_threshold_seconds |

## Related

- [GTFS dataset](/docs/datasets/gtfs.md)
- [Realtime feed monitor](/src/gtfs_realtime/feed_monitor.py)
- [Dynamic graph updater](/src/graph/dynamic_updater.py)

---

Document Control

- Owner: Data Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
