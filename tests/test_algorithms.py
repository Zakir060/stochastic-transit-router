from src.algorithms.astar import astar_shortest_path
from src.algorithms.dijkstra import dijkstra_shortest_path
from src.algorithms.yens import yens_k_shortest_paths
from src.graph.core import DirectedGraph


def build_graph() -> DirectedGraph:
    graph = DirectedGraph()
    for node in ("A", "B", "C", "D"):
        graph.add_node(node, lat=40.0, lon=-73.0)
    graph.add_edge("e1", "A", "B", 1.0)
    graph.add_edge("e2", "B", "D", 1.0)
    graph.add_edge("e3", "A", "C", 1.0)
    graph.add_edge("e4", "C", "D", 1.5)
    graph.add_edge("e5", "A", "D", 5.0)
    return graph


def test_dijkstra_shortest_path() -> None:
    result = dijkstra_shortest_path(build_graph(), "A", "D")
    assert result.nodes == ["A", "B", "D"]
    assert result.cost == 2.0
    assert result.edges == ["e1", "e2"]


def test_astar_shortest_path() -> None:
    result = astar_shortest_path(build_graph(), "A", "D")
    assert result.nodes == ["A", "B", "D"]
    assert result.cost == 2.0


def test_yens_returns_ranked_paths() -> None:
    results = yens_k_shortest_paths(build_graph(), "A", "D", 3)
    assert len(results) == 3
    assert results[0].cost <= results[1].cost <= results[2].cost
    assert results[0].nodes == ["A", "B", "D"]
