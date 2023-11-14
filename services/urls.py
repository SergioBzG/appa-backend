from django.urls import path
from .views import (
    carriage_view,
    service_views,
)


services_urls = [
    path(
        "services/",
        service_views.create_service,
        name="create_list_service"
    ),
    path(
        "services/<int:service_id>/",
        service_views.update_get_service,
        name="create_get_service"
        ),
]

carriage_urls = [

]

packages_urls = [

]

urlpatterns = carriage_urls + packages_urls + services_urls
