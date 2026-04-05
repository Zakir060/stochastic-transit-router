# Graph Reference: Core

| Field | Value |
|---|---|
| Owner | Backend Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

The core graph implementation provides a directed, weighted adjacency structure (`DirectedGraph`) used by routing algorithms.

## Data model

The in-memory graph consists of:

- Nodes keyed by `node_id` with a `node_type` and optional geospatial coordinates.
- Directed edges keyed by `edge_id` with a scalar weight and an `edge_type`.

## Primary interface

| Method | Purpose |
| --- | --- |
| `add_node(node_id, node_type, lat, lon, metadata)` | Insert or replace a node. |
| `add_edge(edge_id, from_node, to_node, weight, edge_type, metadata)` | Insert or replace a directed edge. |
| `neighbors(node_id)` | Return outgoing edges for algorithm traversal. |
| `update_edge_weight(edge_id, weight)` | Update an existing edge weight in place. |
| `status()` | Return a `GraphStatus(node_count, edge_count)` snapshot. |

## Design constraints

- Edge weights are treated as non-negative by the shortest-path solvers in `src/algorithms/`.
- Graph updates are explicit operations; there is no implicit background synchronization with realtime feeds.

## Implementation

- Core implementation: [src/graph/core.py](/src/graph/core.py)
- Node type: [src/graph/node.py](/src/graph/node.py)
- Edge type: [src/graph/edge.py](/src/graph/edge.py)

## Related

- [Graph Model](/docs/math/graph_model.md)
- [Algorithm Reference: Dijkstra](/docs/reference/algorithms/dijkstra.md)
- [Architecture Overview](/docs/architecture/overview.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
