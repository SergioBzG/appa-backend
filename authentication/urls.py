from django.urls import path
from .views.views import *

urlpatterns = [
    path("register/", register_user, name="register_user")
]