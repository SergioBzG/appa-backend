from django.urls import path
from .views.authentication_views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", register_user, name="register_user"),
    path("register/bison", register_bison, name="register_bison"),
    path('login/', login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]