from django.urls import path
from .views.user_views import *

urlpatterns = [
    path("user/services/<int:user_id>/", get_user_services, name="get_user_services"),
    path("user/update/<int:user_id>/", update_user_profile, name="update_user_profile"),
    path("user/delete/<int:user_id>/", delete_user_profile, name="delete_user_profile"),
    path("user/users/", get_users, name="get_users"),
]
