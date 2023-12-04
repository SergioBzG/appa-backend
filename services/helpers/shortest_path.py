from ..helpers.checkpoints import Checkpoint
from ..helpers.graph import graph


import heapq

def find_shortest_path(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]  # Usamos una cola de prioridad (heap)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance_to_neighbor = current_distance + weight

            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))

    # Reconstruir el camino y calcular la distancia total
    path = []
    total_distance = distances[end]
    current_node = end

    while previous_nodes[current_node] is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]

    path.insert(0, start)
    return path, total_distance


