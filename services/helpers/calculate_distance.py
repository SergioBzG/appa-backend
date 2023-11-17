# from typing import Dict, List, Optional
#
# class Checkpoint:
#     NorthernWater = "NorthernWater"
#     SouthernWater = "SouthernWater"
#     NorthernAir = "NorthernAir"
#     EasternAir = "EasternAir"
#     WesternAir = "WesternAir"
#     SouthernAir = "SouthernAir"
#     BaSingSe = "BaSingSe"
#     Abbey = "Abbey"
#     GaipanVillage = "GaipanVillage"
#     SiWong = "SiWong"
#     FireCapital = "FireCapital"
#     ShuJing = "ShuJing"
#
#
# class CheckpointCoordinates:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
#
# def calculate_distance(coord1: CheckpointCoordinates, coord2: CheckpointCoordinates) -> float:
#     dx = coord1.x - coord2.x
#     dy = coord1.y - coord2.y
#     return (dx ** 2 + dy ** 2) ** 0.5
#
# def find_shortest_path(graph: Dict[str, Dict[str, float]], start: str, end: str) -> Optional[List[str]]:
#     distances = {node: 0 if node == start else float('inf') for node in graph}
#     previous_nodes = {node: None for node in graph}
#     nodes = list(graph.keys())
#
#     while nodes:
#         closest_node = min(nodes, key=lambda node: distances[node])
#         if closest_node == end:
#             path = []
#             current_node = end
#             total_distance = 0
#             while current_node != start:
#                 path.insert(0, current_node)
#                 total_distance += graph[current_node][previous_nodes[current_node]]
#                 current_node = previous_nodes[current_node]
#             path.insert(0, start)
#             return path, total_distance
#
#         nodes.remove(closest_node)
#
#         for neighbor, distance in graph[closest_node].items():
#             total_distance = distances[closest_node] + distance
#             if total_distance < distances[neighbor]:
#                 distances[neighbor] = total_distance
#                 previous_nodes[neighbor] = closest_node
#
#     return None
#
# # Crear el diccionario de coordenadas
# coordinates = {
#     Checkpoint.NorthernWater: CheckpointCoordinates(539, 70),
#     Checkpoint.SouthernWater: CheckpointCoordinates(436, 675),
#     Checkpoint.NorthernAir: CheckpointCoordinates(624, 122),
#     Checkpoint.EasternAir: CheckpointCoordinates(907, 433),
#     Checkpoint.WesternAir: CheckpointCoordinates(311, 211),
#     Checkpoint.SouthernAir: CheckpointCoordinates(453, 555),
#     Checkpoint.BaSingSe: CheckpointCoordinates(778, 235),
#     Checkpoint.Abbey: CheckpointCoordinates(456, 221),
#     Checkpoint.GaipanVillage: CheckpointCoordinates(568, 280),
#     Checkpoint.SiWong: CheckpointCoordinates(700, 400),
#     Checkpoint.FireCapital: CheckpointCoordinates(174, 375),
#     Checkpoint.ShuJing: CheckpointCoordinates(435, 321),
# }
#
# # Crear el grafo
# graph = {
#     Checkpoint.FireCapital: {
#         Checkpoint.WesternAir: calculate_distance(coordinates[Checkpoint.FireCapital], coordinates[Checkpoint.WesternAir]),
#         Checkpoint.ShuJing: calculate_distance(coordinates[Checkpoint.FireCapital], coordinates[Checkpoint.ShuJing]),
#         Checkpoint.SouthernAir: calculate_distance(coordinates[Checkpoint.FireCapital], coordinates[Checkpoint.SouthernAir]),
#     },
#     Checkpoint.WesternAir: {
#         Checkpoint.FireCapital: calculate_distance(coordinates[Checkpoint.WesternAir], coordinates[Checkpoint.FireCapital]),
#         Checkpoint.ShuJing: calculate_distance(coordinates[Checkpoint.WesternAir], coordinates[Checkpoint.ShuJing]),
#         Checkpoint.Abbey: calculate_distance(coordinates[Checkpoint.WesternAir], coordinates[Checkpoint.Abbey]),
#     },
#     Checkpoint.Abbey: {
#         Checkpoint.WesternAir: calculate_distance(coordinates[Checkpoint.Abbey], coordinates[Checkpoint.WesternAir]),
#         Checkpoint.ShuJing: calculate_distance(coordinates[Checkpoint.Abbey], coordinates[Checkpoint.ShuJing]),
#         Checkpoint.GaipanVillage: calculate_distance(coordinates[Checkpoint.Abbey], coordinates[Checkpoint.GaipanVillage]),
#         Checkpoint.NorthernWater: calculate_distance(coordinates[Checkpoint.Abbey], coordinates[Checkpoint.NorthernWater]),
#     },
#     Checkpoint.NorthernWater: {
#         Checkpoint.Abbey: calculate_distance(coordinates[Checkpoint.NorthernWater], coordinates[Checkpoint.Abbey]),
#         Checkpoint.NorthernAir: calculate_distance(coordinates[Checkpoint.NorthernWater], coordinates[Checkpoint.NorthernAir]),
#     },
#     Checkpoint.ShuJing: {
#         Checkpoint.FireCapital: calculate_distance(coordinates[Checkpoint.ShuJing], coordinates[Checkpoint.FireCapital]),
#         Checkpoint.WesternAir: calculate_distance(coordinates[Checkpoint.ShuJing], coordinates[Checkpoint.WesternAir]),
#         Checkpoint.Abbey: calculate_distance(coordinates[Checkpoint.ShuJing], coordinates[Checkpoint.Abbey]),
#         Checkpoint.GaipanVillage: calculate_distance(coordinates[Checkpoint.ShuJing], coordinates[Checkpoint.GaipanVillage]),
#         Checkpoint.SiWong: calculate_distance(coordinates[Checkpoint.ShuJing], coordinates[Checkpoint.SiWong]),
#         Checkpoint.SouthernAir: calculate_distance(coordinates[Checkpoint.ShuJing], coordinates[Checkpoint.SouthernAir]),
#     },
#     Checkpoint.NorthernAir: {
#         Checkpoint.NorthernWater: calculate_distance(coordinates[Checkpoint.NorthernAir], coordinates[Checkpoint.NorthernWater]),
#         Checkpoint.BaSingSe: calculate_distance(coordinates[Checkpoint.NorthernAir], coordinates[Checkpoint.BaSingSe]),
#         Checkpoint.GaipanVillage: calculate_distance(coordinates[Checkpoint.NorthernAir], coordinates[Checkpoint.GaipanVillage]),
#         Checkpoint.Abbey: calculate_distance(coordinates[Checkpoint.NorthernAir], coordinates[Checkpoint.Abbey]),
#     },
#     Checkpoint.GaipanVillage: {
#         Checkpoint.NorthernAir: calculate_distance(coordinates[Checkpoint.GaipanVillage], coordinates[Checkpoint.NorthernAir]),
#         Checkpoint.BaSingSe: calculate_distance(coordinates[Checkpoint.GaipanVillage], coordinates[Checkpoint.BaSingSe]),
#         Checkpoint.SiWong: calculate_distance(coordinates[Checkpoint.GaipanVillage], coordinates[Checkpoint.SiWong]),
#         Checkpoint.ShuJing: calculate_distance(coordinates[Checkpoint.GaipanVillage], coordinates[Checkpoint.ShuJing]),
#         Checkpoint.Abbey: calculate_distance(coordinates[Checkpoint.GaipanVillage], coordinates[Checkpoint.Abbey]),
#     },
#     Checkpoint.BaSingSe: {
#         Checkpoint.NorthernAir: calculate_distance(coordinates[Checkpoint.BaSingSe], coordinates[Checkpoint.NorthernAir]),
#         Checkpoint.GaipanVillage: calculate_distance(coordinates[Checkpoint.BaSingSe], coordinates[Checkpoint.GaipanVillage]),
#         Checkpoint.EasternAir: calculate_distance(coordinates[Checkpoint.BaSingSe], coordinates[Checkpoint.EasternAir]),
#     },
#     Checkpoint.SiWong: {
#         Checkpoint.GaipanVillage: calculate_distance(coordinates[Checkpoint.SiWong], coordinates[Checkpoint.GaipanVillage]),
#         Checkpoint.ShuJing: calculate_distance(coordinates[Checkpoint.SiWong], coordinates[Checkpoint.ShuJing]),
#         Checkpoint.SouthernAir: calculate_distance(coordinates[Checkpoint.SiWong], coordinates[Checkpoint.SouthernAir]),
#     },
#     Checkpoint.SouthernAir: {
#         Checkpoint.SiWong: calculate_distance(coordinates[Checkpoint.SouthernAir], coordinates[Checkpoint.SiWong]),
#         Checkpoint.ShuJing: calculate_distance(coordinates[Checkpoint.SouthernAir], coordinates[Checkpoint.ShuJing]),
#         Checkpoint.SouthernWater: calculate_distance(coordinates[Checkpoint.SouthernAir], coordinates[Checkpoint.SouthernWater]),
#         Checkpoint.FireCapital: calculate_distance(coordinates[Checkpoint.SouthernAir], coordinates[Checkpoint.FireCapital]),
#     },
#     Checkpoint.SouthernWater: {
#         Checkpoint.SouthernAir: calculate_distance(coordinates[Checkpoint.SouthernWater], coordinates[Checkpoint.SouthernAir]),
#     },
#     Checkpoint.EasternAir: {
#         Checkpoint.BaSingSe: calculate_distance(coordinates[Checkpoint.EasternAir], coordinates[Checkpoint.BaSingSe]),
#         Checkpoint.SiWong: calculate_distance(coordinates[Checkpoint.EasternAir], coordinates[Checkpoint.SiWong]),
#     },
# }
#
# # Llamar a la funciÃ³n find_shortest_path
# start_checkpoint = Checkpoint.FireCapital
# end_checkpoint = Checkpoint.ShuJing
# shortest_path, total_distance = find_shortest_path(graph, start_checkpoint, end_checkpoint)
#
# print("Shortest Path:", shortest_path)
# print(total_distance)