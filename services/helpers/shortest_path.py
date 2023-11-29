from ..helpers.checkpoints import Checkpoint
from ..helpers.graph import graph


def find_shortest_path(graph: dict[Checkpoint, dict[Checkpoint, float]], start: Checkpoint, end: Checkpoint) -> tuple[list[Checkpoint], float] | None:
    """
    Find the shortest path between two checkpoints and the total distance

    :param graph: graph with checkpoints as nodes and distances as edges
    :param start: start checkpoint of the path
    :param end: end checkpoint of the path
    :return: tuple with the shortest path and the total distance
    """

    distances: dict = {node: 0 if node == start else float('inf') for node in graph}
    previous_nodes: dict = {node: None for node in graph}
    nodes: list[Checkpoint] = list(graph.keys())

    while nodes:
        closest_node = min(nodes, key=lambda node: distances[node])
        if closest_node == end:
            path = []
            current_node = end
            total_distance = 0
            while current_node != start:
                path.insert(0, current_node)
                total_distance += graph[current_node][previous_nodes[current_node]]
                current_node = previous_nodes[current_node]
            path.insert(0, start)
            return path, total_distance

        nodes.remove(closest_node)

        for neighbor, distance in graph[closest_node].items():
            total_distance = distances[closest_node] + distance
            if total_distance < distances[neighbor]:
                distances[neighbor] = total_distance
                previous_nodes[neighbor] = closest_node

    return None