from django.http import JsonResponse
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from authentication.permissions.is_token_valid import IsTokenValid
from services.models import Service
from services.serializers.service_serializer import ServiceSerializer
from ..models.user import User


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsTokenValid])
def get_user_services(request, user_id: int) -> JsonResponse:
    """_summary_

        Args:
            request (_type_): _description_
            user_id (_int_): _description_
        Returns:
            JsonResponse: _description_
    """
    try:
        user: User = User.objects.get(pk=user_id)
        if user.role.name == "CITIZEN":
            user_services: list[Service] = user.citizen_orders.all().order_by("created")
            services_serializer: ServiceSerializer = ServiceSerializer(user_services, many=True)
            return JsonResponse(
                data=services_serializer.data,
                safe=False,
                status=status.HTTP_200_OK
            )
        elif user.role.name == "BISON":
            user_services: list[Service] = user.bison_orders.all().order_by("created")
            services_serializer: ServiceSerializer = ServiceSerializer(user_services, many=True)
            return JsonResponse(
                data=services_serializer.data,
                safe=False,
                status=status.HTTP_200_OK
            )

        return JsonResponse(
            data={"message": "This user can not have services"},
            status=status.HTTP_400_BAD_REQUEST
        )

    except User.DoesNotExist:
        return JsonResponse(
            data={"message": "User does not exist"},
            status=status.HTTP_404_NOT_FOUND
        )