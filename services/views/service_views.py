from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from authentication.permissions.is_token_valid import IsTokenValid
from services.models import Service
from services.serializers.service_serializer import ServiceSerializer


@api_view(["POST"])
def create_get_service(request) -> JsonResponse:
    """

    :param request:
    :return:
    """
    if request.method == "POST":
        request.data["price"] = 0
        serializer: ServiceSerializer = ServiceSerializer(data=request.data)

        if serializer.is_valid():
            service: Service = serializer.save()

            return JsonResponse(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )

        return JsonResponse(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
