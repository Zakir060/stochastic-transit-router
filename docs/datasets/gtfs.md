# GTFS Dataset

| Field | Value |
|---|---|
| Owner | Data Engineering |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This document describes GTFS schedule ingestion requirements, schema mapping, and data quality checks.

## Required GTFS files

| File | Required | Key fields | Foreign keys | Schema reference |
|:--|:--|:--|:--|:--|
| agency.txt | yes | agency_name agency_url agency_timezone | none | [schemas/gtfs/agency.json](/schemas/gtfs/agency.json) |
| stops.txt | yes | stop_id stop_name stop_lat stop_lon | parent_station -> stops.stop_id | [schemas/gtfs/stops.json](/schemas/gtfs/stops.json) |
| routes.txt | yes | route_id route_type | agency_id -> agency.agency_id | [schemas/gtfs/routes.json](/schemas/gtfs/routes.json) |
| trips.txt | yes | trip_id route_id service_id | route_id -> routes.route_id | [schemas/gtfs/trips.json](/schemas/gtfs/trips.json) |
| stop_times.txt | yes | trip_id stop_id stop_sequence | trip_id -> trips.trip_id | [schemas/gtfs/stop_times.json](/schemas/gtfs/stop_times.json) |

## Optional GTFS files

| File | Condition for use | Key fields | Notes |
|:--|:--|:--|:--|
| pathways.txt | station structure available | pathway_id from_stop_id to_stop_id | enables station level walking |
| transfers.txt | transfer policy provided | from_stop_id to_stop_id transfer_type | explicit transfer penalties |
| frequencies.txt | headway service provided | trip_id start_time end_time headway_secs | frequency based modeling |
| shapes.txt | geometry provided | shape_id shape_pt_lat shape_pt_lon | map matching and distance checks |

## Data quality checks

| Field | Check type | Condition | Action on failure |
|:--|:--|:--|:--|
| stop_id | uniqueness | no duplicates | reject feed |
| stop_lat stop_lon | range | lat in [-90,90], lon in [-180,180] | drop invalid rows and log |
| trip_id references | referential integrity | every stop_times trip exists in trips | reject inconsistent rows |
| service date range | temporal sanity | start_date \<= end_date | reject calendar row |

## Related

- [GTFS Realtime dataset](/docs/datasets/gtfs_realtime.md)
- [GTFS schema definitions](/schemas/gtfs/)
- [GTFS validator](/src/gtfs/validator.py)

---

Document Control

- Owner: Data Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
