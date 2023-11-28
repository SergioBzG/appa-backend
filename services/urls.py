from django.urls import path
from .views import (
    service_views,
)

services_urls = [
    path(
        "services/carriage/",
        service_views.create_carriage,
        name="create_carriage"
    ),
    path(
        "services/package/",
        service_views.create_package,
        name="create_package"
    ),
    path(
        "services/<int:service_id>/",
        service_views.update_get_service,
        name="create_get_service"
    ),
    path(
        "services/price/",
        service_views.get_service_price,
        name="get_service_price"
    ),
    path(
        "services/route/",
        service_views.get_route,
        name="get_route"
    ),
    path(
        "service/active/",
        service_views.get_service_active,
        name="get_route"
    ),
    path(
        "service/track/<int:guide>",
        service_views.track_service,
        name="get_route"
    ),
]

carriage_urls = [

]

packages_urls = [

]

urlpatterns = carriage_urls + packages_urls + services_urls
