# Algorithm Reference: Time-dependent Shortest Path

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

The time-dependent shortest-path solver generalizes Dijkstra-style search to handle edge costs that depend on the current departure time.

## Interface

```python
from src.algorithms.time_dependent import time_dependent_shortest_path

result = time_dependent_shortest_path(
	graph,
	source="A",
	target="D",
	departure_time=1712318400,
)
```

To inject a time-dependent edge cost model, pass a `weight_function`:

```python
def weight_function(edge, current_time: int) -> float:
	return edge.weight

result = time_dependent_shortest_path(
	graph,
	source="A",
	target="D",
	departure_time=1712318400,
	weight_function=weight_function,
)
```

## Constraints

- The solver assumes non-negative evaluated edge costs.
- The time update step uses `current_time + int(edge_cost)`; if you model non-integer seconds, define a consistent rounding policy in the weight function.

## Complexity

Time complexity remains $O((|V| + |E|)\\log|V|)$ in the number of evaluated edges, with $O(|V|)$ auxiliary space.

## Implementation

- Implementation: [src/algorithms/time_dependent.py](/src/algorithms/time_dependent.py)
- Graph type: [src/graph/core.py](/src/graph/core.py)

## Related

- [Graph Model: Time-dependent Edge Weight](/docs/math/graph_model.md)
- [Graph Reference: Temporal Graph](/docs/reference/graph/temporal.md)

---

Document Control

- Owner: Algorithm Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
