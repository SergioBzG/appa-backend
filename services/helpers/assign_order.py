from django.utils import timezone
from appa_admin.models.user import User
from services.models.service import Service


def search_for_bison(service: Service) -> User | None:
    """Search for an available bison to assign to the service

    :param service: Service to assign a bison to
    :return User: User with BISON role selected to delivery the service
    """
    bisons: list[User] = User.objects.filter(role__name="BISON", available=True)
    min_date: timezone = timezone.now()
    selected_bison: User = None
    for bison in bisons:
        if not bison.bison_orders.all().count():
            # if bison never has had a service, it will be the first one
            bison.bison_orders.add(service)
            bison.available = False
            bison.save(update_fields=["available"])
            return bison

        else:
            # if bison has had services assigned before
            last_order: Service = bison.bison_orders.all().order_by("-arrived").first()
            if last_order.arrived < min_date:
                min_date = last_order.arrived
                selected_bison = bison

    if selected_bison:
        selected_bison.bison_orders.add(service)
        selected_bison.available = False
        selected_bison.save(update_fields=["available"])

    return selected_bison


def search_for_order(bison: User) -> Service | None:
    """Search for an order on waiting list to assign to the bison

    :param bison: User with BISON role to assign a service to
    :return: Service selected to be delivered by the bison
    """
    order: Service | None = Service.objects.filter(user_bison=None, arrived__isnull=True).order_by("created").first()

    if order:
        order.user_bison = bison
        order.save(update_fields=["user_bison"])

    return order