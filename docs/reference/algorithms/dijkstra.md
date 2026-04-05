# Algorithm Reference: Dijkstra Shortest Path

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

Dijkstra's algorithm computes a minimum-cost path in a directed graph with non-negative edge weights.

## Interface

```python
from src.algorithms.dijkstra import dijkstra_shortest_path

result = dijkstra_shortest_path(graph, source="A", target="D")
```

### Inputs

- `graph`: a `DirectedGraph` instance.
- `source`, `target`: node ids.

### Output

Returns a `PathResult` containing:

- `nodes`: ordered path nodes, or an empty list when no path exists.
- `cost`: total weight sum.
- `edges`: edge ids along the chosen path when reconstructable.

## Complexity

Time complexity is $O((|V| + |E|)\\log|V|)$ using a binary heap, with $O(|V|)$ auxiliary space.

## Constraints

- All edge weights must be non-negative; negative weights raise `ValueError`.

## Implementation

- Implementation: [src/algorithms/dijkstra.py](/src/algorithms/dijkstra.py)
- Graph type: [src/graph/core.py](/src/graph/core.py)
- Path model: [src/models/path.py](/src/models/path.py)

## Related

- [API Reference: Routes](/docs/reference/api/routes.md)
- [Algorithm Reference: A\*](/docs/reference/algorithms/astar.md)
- [Graph Reference: Core](/docs/reference/graph/core.md)

---

Document Control

- Owner: Algorithm Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
