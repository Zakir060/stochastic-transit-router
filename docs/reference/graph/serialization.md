# Graph Reference: Serialization

| Field | Value |
|---|---|
| Owner | Backend Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

Graph serialization defines how an in-memory graph is persisted as an artifact under `data/processed/` so that API and benchmark runs can use a consistent snapshot.

## Current status

The serializer module is currently scaffolded. The repository already defines schema boundaries for processed artifacts, and the operational scripts generate graph-adjacent seed artifacts (see `scripts/build_graph_nyc.py`). Full graph serialization will evolve from these outputs.

## Implementation

- Serializer scaffold: [src/graph/serializer.py](/src/graph/serializer.py)
- Graph seed builder script: [scripts/build_graph_nyc.py](/scripts/build_graph_nyc.py)
- Graph processed artifacts: [data/processed/README.md](/data/processed/README.md)

## Related

- [Graph Representation ADR](/docs/adr/0002_graph_representation.md)
- [Storage Approach ADR](/docs/adr/0007_storage_approach.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
