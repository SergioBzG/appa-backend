from django.urls import path, re_path
from .views.user_views import *

urlpatterns = [
    path("user/services/<int:user_id>/", get_user_services, name="get_user_services"),
    path("user/update/<int:user_id>/", update_user_profile, name="update_user_profile"),
    path("user/delete/<int:user_id>/", delete_user_profile, name="delete_user_profile"),
    re_path(r"^user/services/(?P<user_id>\d+)(?:/(?P<type>package|carriage))?/$",
            get_user_services,
            name="get_user_services"),
    path("user/last-service/<int:user_id>/",
         get_user_last_service,
         name="get_bison_last_service"
         ),
]
