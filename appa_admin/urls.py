from django.urls import path, re_path
from .views.user_views import *

urlpatterns = [
    re_path(r"^user/services/(?P<user_id>\d+)(?:/(?P<type>package|carriage))?/$",
            get_user_services,
            name="get_user_services"),
]
