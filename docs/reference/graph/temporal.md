# Graph Reference: Temporal Graph

| Field | Value |
|---|---|
| Owner | Backend Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

Temporal graph support is the layer that will generalize scalar edge weights to departure-time dependent weight functions $w_e(t)$.

## Current status

The temporal graph module is currently scaffolded and does not yet implement a time-dependent edge evaluation API. Time-dependent routing is supported today by injecting a `weight_function(edge, time)` into the solver (see the algorithm reference).

## Implementation

- Temporal graph scaffold: [src/graph/temporal_graph.py](/src/graph/temporal_graph.py)
- Time-dependent solver: [src/algorithms/time_dependent.py](/src/algorithms/time_dependent.py)

## Related

- [Graph Model: Time-dependent Edge Weight](/docs/math/graph_model.md)
- [Algorithm Reference: Time-dependent Shortest Path](/docs/reference/algorithms/time_dependent.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
