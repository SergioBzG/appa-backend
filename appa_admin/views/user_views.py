from django.http import JsonResponse, Http404
from authentication.models import Role
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

        user_last_service: Service = user.citizen_orders.all().order_by("-created").first()

        serializer: ServiceSerializer = ServiceSerializer(user_last_service)

        return JsonResponse(
            data=serializer.data,
            status=status.HTTP_200_OK
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


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsTokenValid])
def get_users(request):
    try:
        role = request.query_params.get('role')
        user_id = request.query_params.get('id')

        queryset = User.objects.all()

        if role:
            role: int = Role.objects.get(name=role)
            queryset = queryset.filter(role_id=role)

        if user_id:
            queryset = queryset.filter(id=user_id).first()
            serializer = UserSerializer(queryset)
            return JsonResponse(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        if not queryset:
            raise Http404("No users found")

        serializer = UserSerializer(queryset, many=True)

        return JsonResponse(
            data=serializer.data,
            safe=False,
            status=status.HTTP_200_OK
        )

    except Http404 as e:
        return JsonResponse(
            data={"message": str(e)},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
