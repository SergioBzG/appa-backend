from django.http import JsonResponse
from authentication.permissions.role_permissions import IsCitizen
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from authentication.permissions.is_token_valid import IsTokenValid
from services.models import Service
from services.serializers.service_serializer import ServiceSerializer
from ..models.user import User
from ..serializers.user_serializer import UserSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsTokenValid, ~IsAdminUser])
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
        if user != request.user:
            return JsonResponse(
                data={"message": "Incorrect user id"},
                status=status.HTTP_403_FORBIDDEN
            )

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


@api_view(["PATCH"])
@permission_classes([IsAuthenticated, IsTokenValid, ~IsAdminUser])
def update_user_profile(request, user_id: int) -> JsonResponse:
    try:
        user: User = User.objects.get(pk=user_id)
        request.data["role"]: int = user.role.id
        if user != request.user:
            return JsonResponse(
                data={"message": "Incorrect user id"},
                status=status.HTTP_403_FORBIDDEN
            )

        user_serializer: UserSerializer = UserSerializer(user, data=request.data, partial=True)

        if user_serializer.is_valid():
            user_serializer.save()
            data: dict = {"message": "User updated successfully", "user": user_serializer.data}
            return JsonResponse(data=data, status=status.HTTP_200_OK)

        return JsonResponse(
            data=user_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    except User.DoesNotExist:
        return JsonResponse(
            data={"message": "User does not exist"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsTokenValid, IsCitizen | IsAdminUser])
def delete_user_profile(request, user_id: int) -> JsonResponse:
    try:
        user: User = User.objects.get(pk=user_id)
        if user != request.user:
            if request.user.is_staff:
                pass
            else:
                return JsonResponse(
                    data={"message": "Incorrect user id"},
                    status=status.HTTP_403_FORBIDDEN
                )

        user.delete()
        return JsonResponse(
            data={"message": "User deleted"},
            status=status.HTTP_204_NO_CONTENT
        )

    except User.DoesNotExist:
        return JsonResponse(
            data={"message": "User does not exist"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
