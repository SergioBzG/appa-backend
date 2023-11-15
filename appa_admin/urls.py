from django.urls import path
from .views.user_views import *

urlpatterns = [
  path("user/services/<int:user_id>/", get_user_services, name="get_user_services"),
]