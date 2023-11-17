# import heapq
# from math import inf
# from Graph import Graph
# from Node import Node
# from collections import deque
#
#
# def find_path_flight(node_origin: int, node_destination: int):
#     path_flight = deque([])
#     NO_PARENT = -1
#
#     graphSPD: dict = dict([(i, inf) for i in range(Node.nodes_quantity)])
#     graphSPD[node_origin] = 0
#     parents = [-1] * Node.nodes_quantity
#
#     # Start Dijkstra
#     queue: list = []
#     heapq.heappush(queue, (0, node_origin))  # (SPD, node)
#     while len(queue) > 0:
#         spdU, u = heapq.heappop(queue)
#         for v, d in Graph.graph[u].items():
#             if spdU + d < graphSPD[v]:
#                 graphSPD[v] = spdU + d
#                 heapq.heappush(queue, (graphSPD[v], v))
#                 parents[v] = u
#
#     def print_path(current_vertex, parents_data):
#         # Base case : Source node has
#         # been processed
#         if current_vertex == NO_PARENT:
#             return
#         print_path(parents_data[current_vertex], parents_data)
#         path_flight.append(current_vertex)
#
#     print_path(node_destination, parents)
#     return path_flight, graphSPD[node_destination]