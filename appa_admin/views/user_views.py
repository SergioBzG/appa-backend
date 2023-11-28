from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from authentication.permissions.is_token_valid import IsTokenValid
from authentication.permissions.role_permissions import IsCitizen
from services.models import Service
from services.serializers.service_serializer import ServiceSerializer
from ..models.user import User


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsTokenValid, ~IsAdminUser])
def get_user_services(request, user_id: int, type: str = "") -> JsonResponse:
    """

    :param request:
    :param user_id:
    :param type:
    :return:
    """
    try:
        user: User = User.objects.get(pk=user_id)
        if user != request.user:
            return JsonResponse(
                data={"message": "Incorrect user id"},
                status=status.HTTP_403_FORBIDDEN
            )

        if user.role.name == "CITIZEN":
            user_services: list[Service] = user.citizen_orders.all().order_by("created")
        elif user.role.name == "BISON":
            user_services: list[Service] = user.bison_orders.all().order_by("created")

        if type:
            user_services = user_services.filter(type=type.upper())

        serializer: ServiceSerializer = ServiceSerializer(user_services, many=True)

        return JsonResponse(
            data=serializer.data,
            safe=False,
            status=status.HTTP_200_OK
        )

    except User.DoesNotExist:
        return JsonResponse(
            data={"message": "User does not exist"},
            status=status.HTTP_404_NOT_FOUND
        )
    
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsTokenValid, IsCitizen])
def get_user_last_service(request, user_id: int) -> JsonResponse:
    """

    :param request:
    :param user_id:
    :return:
    """
    try:
        user: User = User.objects.get(pk=user_id)
        if user != request.user:
            return JsonResponse(
                data={"message": "Incorrect user id"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        user_services: list[Service] = user.citizen_orders.all().order_by("created")
        user_last_service = user_services[-1]

        serializer: ServiceSerializer = ServiceSerializer(user_last_service, many=True)

        return JsonResponse(
            data=serializer.data,
            safe=False,
            status=status.HTTP_200_OK
        )
        
    except User.DoesNotExist:
        return JsonResponse(
            data={"message": "User does not exist"},
            status=status.HTTP_404_NOT_FOUND
        )