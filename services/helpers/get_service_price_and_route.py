from .shortest_path import find_shortest_path
from .checkpoints import Checkpoint
from .graph import graph
from services.models import Service


def get_service_price_and_route(service: Service) -> tuple[int, str]:
    """
    Calculate the price and optimal route of a service. The price calculation depends on the type of service.

    :param service: service to which the price and route will be gotten
    :return: tuple with the price and the optimal route (price, route)
    """
    start_checkpoint = Checkpoint(service.origin_checkpoint)
    end_checkpoint = Checkpoint(service.destiny_checkpoint)
    shortest_path, total_distance = find_shortest_path(graph, start_checkpoint, end_checkpoint)

    price: int = 0
    if service.type == "CARRIAGE":
        # 1070 is the price per kilometer
        price = int(total_distance * 1070)
    elif service.type == "PACKAGE":
        pass

    # Turn the route into a string
    route: str = ", ".join(map(lambda checkpoint: checkpoint.value, shortest_path))

    return price, route

