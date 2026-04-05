# Algorithm Reference: A* Shortest Path

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

A\* is a best-first shortest-path algorithm that uses a heuristic lower bound to reduce the explored search space. In this repository, the heuristic is the haversine distance between node coordinates divided by an upper bound on speed.

## Interface

```python
from src.algorithms.astar import astar_shortest_path

result = astar_shortest_path(graph, source="A", target="D")
```

## Heuristic

For node $v$ and destination $d$:

$$
h(v) = \\frac{\\mathrm{dist_hav}(v, d)}{v\_{\\max}}
$$

When $v\_{\\max}$ is a valid upper bound on network speed, $h$ is admissible and A\* preserves optimality.

## Complexity

In sparse graphs, the typical complexity is $O((|V| + |E|)\\log|V|)$ with $O(|V|)$ auxiliary space, with performance dependent on heuristic tightness.

## Implementation

- Implementation: [src/algorithms/astar.py](/src/algorithms/astar.py)
- Heuristic: [src/algorithms/heuristics.py](/src/algorithms/heuristics.py)
- Graph type: [src/graph/core.py](/src/graph/core.py)

## Related

- [Graph Model: A\* Heuristic](/docs/math/graph_model.md)
- [Algorithm Reference: Dijkstra](/docs/reference/algorithms/dijkstra.md)

---

Document Control

- Owner: Algorithm Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
