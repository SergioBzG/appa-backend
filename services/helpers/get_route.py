from .shortest_path import find_shortest_path
from .checkpoints import Checkpoint
from .graph import graph


def get_optimal_route(origin_checkpoint: Checkpoint, destiny_checkpoint: Checkpoint) -> list[str]:
    """
    Get optimal route from origin checkpoint to destiny checkpoint

    :param origin_checkpoint: point where route starts
    :param destiny_checkpoint: point where route ends
    :return: price of carriage
    """
    shortest_path, total_distance = find_shortest_path(graph, origin_checkpoint, destiny_checkpoint)

    route: list[str] = [checkpoint.value for checkpoint in shortest_path]

    return route
