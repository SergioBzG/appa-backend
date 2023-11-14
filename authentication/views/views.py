from django.http import JsonResponse
from django.contrib.auth import logout
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from ..permissions.is_token_valid import IsTokenValid

from ..models import BlackListedToken
from appa_admin.models import User
from authentication.models.role import Role

from appa_admin.serializers.user_serializer import UserSerializer
from authentication.serializers.user_login_serializer import UserLoginSerializer

from ..helpers.create_token import get_tokens_for_user


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsTokenValid])
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
def login(request) -> JsonResponse:
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        JsonResponse: _description_
    """
    login_serializer: UserLoginSerializer = UserLoginSerializer(data=request.data)

    if login_serializer.is_valid(raise_exception=True):
        user: User = login_serializer.validated_data
        user_serializer: UserSerializer = UserSerializer(user)
        data: dict = user_serializer.data
        data["tokens"]: dict = get_tokens_for_user(user)

        return JsonResponse(
            data=data,
            status=status.HTTP_200_OK
        )

    return JsonResponse(
        data=login_serializer.errors,
        status=status.HTTP_401_UNAUTHORIZED
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
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

