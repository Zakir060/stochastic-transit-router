# OSM Overpass Dataset

| Field | Value |
|---|---|
| Owner | Data Engineering |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This document describes Overpass extraction rules for pedestrian connectors around transit stops.

## OSM element types

| Element | highway tag value | Role | Walking edge weight formula |
|:--|:--|:--|:--|
| way | footway | sidewalk connector | path_length_m / walk_speed_ms |
| way | pedestrian | plaza or pedestrian street | path_length_m / walk_speed_ms |
| way | path | generic path connector | path_length_m / walk_speed_ms |
| way | steps | stair connector | path_length_m / adjusted_step_speed |
| node or way | crossing | crossing penalty context | base_walk_time plus crossing_penalty |

## Walking edge formula

$$
w\_{walk} = \\frac{haversine(u,v)}{walk_speed_ms}
$$

## Overpass query parameters

| Parameter | Default | Description | Config key |
|:--|:--|:--|:--|
| timeout | 120 | max query execution time | configs/feeds/osm.yaml query.timeout_seconds |
| radius meters | 400 | stop neighborhood search radius | configs/feeds/osm.yaml query.radius_meters |
| min delay seconds | 10 | fair use delay between calls | configs/feeds/osm.yaml fair_use.min_seconds_between_queries |
| retries | 3 | transient failure retries | configs/feeds/osm.yaml fair_use.retry_attempts |

## Related

- [Overpass query builder](/src/osm/query_builder.py)
- [Walking edge builder](/src/osm/walking_edge_builder.py)
- [Graph model](/docs/math/graph_model.md)

---

Document Control

- Owner: Data Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
