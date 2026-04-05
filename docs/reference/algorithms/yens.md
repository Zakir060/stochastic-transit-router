# Algorithm Reference: Yen's $k$-Shortest Loopless Paths

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

Yen's algorithm computes up to $k$ loopless candidate paths, ordered by total cost. It is used to support top-$k$ route enumeration.

## Interface

```python
from src.algorithms.yens import yens_k_shortest_paths

paths = yens_k_shortest_paths(graph, source="A", target="D", k=3)
```

## Complexity

When Dijkstra is used as the subroutine, the typical complexity is:

$$
O\\bigl(k \\cdot n \\cdot (m + n\\log n)\\bigr)
$$

where $n=|V|$ and $m=|E|$.

## Implementation notes

- The current implementation deep-copies the graph for spur path exploration and modifies the adjacency list to suppress edges that would duplicate a previously selected prefix.
- Candidate deduplication is performed by comparing node sequences.

## Implementation

- Implementation: [src/algorithms/yens.py](/src/algorithms/yens.py)
- Subroutine: [src/algorithms/dijkstra.py](/src/algorithms/dijkstra.py)

## Related

- [API Reference: Top-k Routes](/docs/reference/api/topk.md)
- [Algorithm Selection ADR](/docs/adr/0009_algorithm_selection.md)

---

Document Control

- Owner: Algorithm Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
