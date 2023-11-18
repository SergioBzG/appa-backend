from math import pi
from .shortest_path import find_shortest_path
from .checkpoints import Checkpoint
from .graph import graph


def get_carriage_price(origin_checkpoint: Checkpoint, destiny_checkpoint: Checkpoint) -> int:
    """
    Calculate the price of a carriage

    :param origin_checkpoint: point where carriage route starts
    :param destiny_checkpoint: point where carriage route ends
    :return: price of carriage
    """
    shortest_path, total_distance = find_shortest_path(graph, origin_checkpoint, destiny_checkpoint)

    # 1070 is the price per kilometer
    price: int = int(total_distance * 1070)

    return price


def get_package_price(origin_checkpoint: Checkpoint, destiny_checkpoint: Checkpoint, package: dict) -> int:
    """
    Calculate the price of a package

    :param origin_checkpoint: point where carriage route starts
    :param destiny_checkpoint: point where carriage route ends
    :param package: package dimensions and weight
    :return: price of package
    """

    shortest_path, total_distance = find_shortest_path(graph, origin_checkpoint, destiny_checkpoint)

    base_price_short_distance: int = 20000
    base_price_long_distance: int = 50000
    base_price_small_volume: int = 7000
    base_price_big_volume: int = 10000
    short_distance: int = 80

    volume: int = package["height"] * package["width"] * package["length"]
    dimension_price: int = base_price_big_volume if volume > package["weight"] else base_price_small_volume

    if total_distance >= short_distance:
        return int(base_price_long_distance + total_distance * pi)

    return int(base_price_short_distance + dimension_price)
