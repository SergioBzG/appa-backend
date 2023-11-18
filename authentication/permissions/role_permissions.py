from rest_framework.permissions import BasePermission

from authentication.models import Role


class IsBison(BasePermission):
    message: str = "Only users with BISON role are allowed to perform this action"

    def has_permission(self, request, view):
        role: Role = request.user.role
        is_allowed_user: bool = True

        if role.name == "BISON":
            return is_allowed_user

        return not is_allowed_user


class IsCitizen(BasePermission):
    message: str = "Only users with CITIZEN role are allowed to perform this action"

    def has_permission(self, request, view):
        role: Role = request.user.role
        is_allowed_user: bool = True

        if role.name == "CITIZEN":
            return is_allowed_user

        return not is_allowed_user
