from appa_admin.models import User
from services.models import Service


def release_bison(user: User) -> None:
    """
    Release all bison related with services of the user
    :param user: Used that will be deleted
    :return: None
    """
    services: list[Service] = user.citizen_orders.filter(arrived__isnull=True)

    for service in services:
        service.user_bison.available = True
        service.user_bison.save(update_fields=["available"])

