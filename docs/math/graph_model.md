# Graph Model

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This document defines the formal graph model used by stochastic-transit-router for deterministic, time-dependent, and dynamic transit routing, and links each mathematical concept to implementation modules that will carry the corresponding logic.

Let $G = (V, E)$ be a directed graph where $V$ is the set of typed transit nodes and $E$ is the set of typed movement or transfer edges. For any edge $e \in E$ and departure time $t$, the travel-time weight is denoted by $w_e(t)$.

## Node types

| Type | Symbol | Description | Example |
|:--|:--|:--|:--|
| transit_stop | $v_{\text{stop}}$ | Canonical stop in GTFS stops table | MTA stop id 127N |
| station_entrance | $v_{\text{ent}}$ | Entrance node used for multi-level station modeling | Main entrance at Times Sq station |
| platform | $v_{\text{plat}}$ | Boarding and alighting platform node | Downtown platform at a subway station |
| transfer_point | $v_{\text{xfer}}$ | Logical node used to model in-station or cross-route transfer | Interchange between route A and route C |
| pedestrian_connector | $v_{\text{walk}}$ | OSM-derived connector node for walking segments | Footpath crossing near station complex |
| virtual_origin | $v_o$ | Query-time injected source node | User-selected origin coordinate snapped to network |
| virtual_destination | $v_d$ | Query-time injected destination node | User-selected destination coordinate snapped to network |

## Edge types

| Type | Symbol | Weight function | Notes |
|:--|:--|:--|:--|
| scheduled_movement | $e_{\text{sched}}$ | $w_e(t)$ from GTFS stop_times | Baseline in static timetable routing |
| transfer_edge | $e_{\text{xfer}}$ | $t_{\text{transfer}}$ | Explicit transfer rule or minimum transfer time |
| waiting_edge | $e_{\text{wait}}$ | headway or wait estimate | Used in time-expanded and frequency models |
| footpath_edge | $e_{\text{walk}}$ | $w_{\text{walk}}(u, v, t)$ | Built from OSM paths with haversine fallback |
| disruption_adjusted_edge | $e_{\text{disr}}$ | $w_e^{\text{base}}(t) + \delta_e(t) + p_e(t)$ | Captures active disruptions and delay injections |
| service_alert_edge | $e_{\text{alert}}$ | $p_{\text{alert},e}(t)$ | Soft or hard closure semantics via penalty factor |
| boarding_edge | $e_{\text{board}}$ | $c_{\text{board}}(t)$ | Transition from platform wait state to vehicle state |
| alighting_edge | $e_{\text{alight}}$ | $c_{\text{alight}}(t)$ | Transition from vehicle state to platform state |

## Deterministic edge weight

$$w_e(t) = w_{e,\text{scheduled}}(t)$$

The deterministic definition is implemented in [src/graph/core.py](/src/graph/core.py) and consumed by [src/algorithms/dijkstra.py](/src/algorithms/dijkstra.py).

## Time-dependent edge weight

$$w_e(t) = f\left(\text{schedule}, \text{delay}(t), \text{traffic\_profile}(t), \text{time\_of\_day}(t)\right)$$

This generalization is implemented in [src/graph/temporal_graph.py](/src/graph/temporal_graph.py) and [src/algorithms/time_dependent.py](/src/algorithms/time_dependent.py).

## Heuristic for A\* on temporal transit graph

For node $v$ and destination node $d$, let $\text{dist}_{\text{hav}}(v, d)$ be haversine distance in meters and let $v_{\max}$ be an upper bound on network speed in meters per second.

$$h(v) = \frac{\text{dist}_{\text{hav}}(v, d)}{v_{\max}}$$

Admissibility sketch:

- True transit travel time from $v$ to $d$ is lower-bounded by physical distance divided by maximum feasible speed.
- $\text{dist}_{\text{hav}}(v, d)$ is a lower bound on path length in the absence of teleportation.
- Therefore $h(v)$ never overestimates the true remaining cost, so $h$ is admissible when $v_{\max}$ is a valid upper bound.

The heuristic and admissibility checks are implemented in [src/algorithms/heuristics.py](/src/algorithms/heuristics.py) and tested in [tests/unit/algorithms/test_astar.py](/tests/unit/algorithms/test_astar.py).

## Graph notation

| Symbol | Meaning | Domain |
|:--|:--|:--|
| $G$ | Directed transit graph | Graph object |
| $V$ | Set of graph nodes | Finite set |
| $E$ | Set of graph edges | Finite set |
| $v$ | Node element | $v \in V$ |
| $e$ | Edge element | $e \in E$ |
| $t$ | Departure time | Real time axis |
| $w_e(t)$ | Edge weight at departure time $t$ | Non-negative real |
| $d(v, t)$ | Time-dependent value function to destination | Non-negative real |

## Related

- [Stochastic routing](/docs/math/stochastic_routing.md)
- [Risk metrics](/docs/math/risk_metrics.md)
- [ADR 0002: Graph representation](/docs/adr/0002_graph_representation.md)
- [ADR 0014: City generalization](/docs/adr/0014_city_generalization.md)

---

Document Control

- Owner: Research Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
