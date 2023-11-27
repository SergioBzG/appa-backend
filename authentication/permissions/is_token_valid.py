from rest_framework.permissions import BasePermission

from authentication.models.black_list import BlackListedToken


class IsTokenValid(BasePermission):
    message: str = "Invalid token"

    def has_permission(self, request, view):
        user_id: int = request.user.id
        is_allowed_user: bool = True
        token: str = request.auth
        try:
            is_black_listed: BlackListedToken = BlackListedToken.objects.get(user=user_id, token=token)
            if is_black_listed:
                is_allowed_user = False
        except BlackListedToken.DoesNotExist:
            is_allowed_user = True
        return is_allowed_user
