# Graph Reference: Dynamic Updates

| Field | Value |
|---|---|
| Owner | Backend Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

Dynamic updates describe how the graph is adjusted in response to realtime delay information, service alerts, and operational disruptions.

## Update categories

| Update | Typical input | Intended graph action |
| --- | --- | --- |
| Delay injection | GTFS-Realtime `TripUpdate` delays | Adjust weights of affected movement edges. |
| Disruption penalty | Service alert and incident feeds | Add penalty factors or closures via edge metadata. |
| Elevator/escalator status | Station equipment feeds | Adjust station transfer/walking costs. |

## Current status

The dynamic update module is currently scaffolded. Realtime ingestion is implemented at the data acquisition level (snapshot download and manifesting), but automatic online graph mutation is not yet wired into the runtime graph.

## Implementation

- Dynamic update scaffold: [src/graph/dynamic_updater.py](/src/graph/dynamic_updater.py)
- Realtime dataset docs: [GTFS Realtime Dataset](/docs/datasets/gtfs_realtime.md)

## Related

- [Realtime Feed Strategy ADR](/docs/adr/0010_realtime_feed_strategy.md)
- [Online Update Policy ADR](/docs/adr/0013_online_update_policy.md)
- [Data Refresh](/docs/operations/data_refresh.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
