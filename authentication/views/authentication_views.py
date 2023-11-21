from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from ..permissions.is_token_valid import IsTokenValid

from ..models import BlackListedToken, Role
from appa_admin.serializers.user_serializer import UserSerializer


@api_view(["POST"])
def register_user(request) -> JsonResponse:
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        JsonResponse: _description_
    """
    try:
        role: Role = Role.objects.get(name="CITIZEN")
        request.data["role"]: int = role.id
        serializer: UserSerializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Role.DoesNotExist:
        return JsonResponse(
            data={"message": f"{request.data['role']} role does not exist."},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsTokenValid])
def user_logout(request) -> JsonResponse:
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        JsonResponse: _description_
    """
    BlackListedToken.objects.create(user=request.user, token=request.auth)
    return JsonResponse(
        data={"message": "User logged out successfully"},
        status=status.HTTP_200_OK
    )

