from django.http import JsonResponse, Http404
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from authentication.models import Role
from authentication.permissions.is_token_valid import IsTokenValid
from authentication.permissions.role_permissions import IsCitizen, IsBison

from ..helpers.get_service_price import get_carriage_price, get_package_price
from ..helpers.get_route import get_optimal_route
from ..helpers.assign_order import search_for_bison, search_for_order
from ..helpers.checkpoints import Checkpoint

from appa_admin.models import User
from ..models import Service, Guide

from ..serializers.carriage_serializer import CarriageSerializer
from ..serializers.guide_serializer import GuideSerializer
from ..serializers.package_serializer import PackageSerializer
from ..serializers.service_serializer import ServiceSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsTokenValid, IsCitizen])
def create_carriage(request) -> JsonResponse:
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        JsonResponse: _description_
    """
    try:
        if request.data["user_citizen"] != request.user.id:
            return JsonResponse(
                data={"message": "Incorrect user id"},
                status=status.HTTP_403_FORBIDDEN
            )
        service: Service = None
        service_serializer: ServiceSerializer = ServiceSerializer(data=request.data)

        if service_serializer.is_valid():
            service = service_serializer.save()
            # Search for an available bison to assign to the service
            bison: User | None = search_for_bison(service)
            if bison:
                service.user_bison = bison
                service.save(update_fields=["user_bison"])

            Guide.objects.create(
                service=service,
                current_nation=service.origin_nation,
                current_checkpoint=service.origin_checkpoint
            )
            request.data["carriage"]["service"] = service.id
            carriage_serializer = CarriageSerializer(data=request.data["carriage"])

            if carriage_serializer.is_valid():
                carriage_serializer.save()
                return JsonResponse(
                    data=service_serializer.data,
                    status=status.HTTP_201_CREATED
                )

            service.delete()
            return JsonResponse(
                data=carriage_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        return JsonResponse(
            data=service_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    except KeyError:
        return JsonResponse(
            data={"message": f"Missing required fields"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        if service:
            service.delete()
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsTokenValid, IsCitizen])
def create_package(request) -> JsonResponse:
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        JsonResponse: _description_
    """
    try:
        if request.data["user_citizen"] != request.user.id:
            return JsonResponse(
                data={"message": "Incorrect user id"},
                status=status.HTTP_403_FORBIDDEN
            )
        service: Service = None
        service_serializer: ServiceSerializer = ServiceSerializer(data=request.data)

        if service_serializer.is_valid():
            service = service_serializer.save()
            # Search for an available bison to assign to the service
            bison: User | None = search_for_bison(service)
            if bison:
                service.user_bison = bison
                service.save(update_fields=["user_bison"])

            Guide.objects.create(
                service=service,
                current_nation=service.origin_nation,
                current_checkpoint=service.origin_checkpoint
            )
            request.data["package"]["service"] = service.id
            package_serializer = PackageSerializer(data=request.data["package"])

            if package_serializer.is_valid():
                package_serializer.save()
                return JsonResponse(
                    data=service_serializer.data,
                    status=status.HTTP_201_CREATED
                )

            service.delete()
            return JsonResponse(
                data=package_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        return JsonResponse(
            data=service_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    except KeyError:
        return JsonResponse(
            data={"message": f"Missing required fields"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        if service:
            service.delete()
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["PATCH"])
@permission_classes([IsAuthenticated, IsTokenValid, IsBison])
def update_service(request, service_id: int) -> JsonResponse:
    """_summary_

        Args:
            request (_type_): _description_
            service_id (_int_): _description_
        Returns:
            JsonResponse: _description_
    """
    try:
        service: Service = Service.objects.get(id=service_id)
        if service.user_bison.id != request.user.id:
            return JsonResponse(
                data={"message": "You do not have a service assigned with this id"},
                status=status.HTTP_403_FORBIDDEN
            )

        guide: Guide = service.guide
        guide.current_nation = request.data["current_nation"]
        guide.current_checkpoint = request.data["current_checkpoint"]
        guide.save(update_fields=["current_nation", "current_checkpoint"])
        if guide.current_checkpoint == service.destiny_checkpoint:
            service.arrived = timezone.now()
            service.save(update_fields=["arrived"])
            # Now the bison is available again
            bison: User = request.user
            bison.available = True
            bison.save(update_fields=["available"])
            # Search for an order to assign to the bison
            order: Service | None = search_for_order(bison)
            if order:
                bison.bison_orders.add(order)
                bison.available = False
                bison.save(update_fields=["available"])
        if service.type == "CARRIAGE" and "price" in request.data:
            service.price = request.data["price"]
            service.save(update_fields=["price"])
        serializer: ServiceSerializer = ServiceSerializer(service)
        data: dict = {"message": "Service updated successfully", "service": serializer.data}
        return JsonResponse(data=data, status=status.HTTP_200_OK)

    except Service.DoesNotExist:
        return JsonResponse(
            data={"message": "Service does not exist"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except KeyError:
        return JsonResponse(
            data={"message": "Missing required fields"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsTokenValid, ~IsAdminUser])
def get_service(request, service_id: int) -> JsonResponse:
    """_summary_

    Args:
        request (_type_): _description_
        service_id (_type_): _description_

    Returns:
        JsonResponse: _description_
    """
    try:
        service: Service = Service.objects.get(id=service_id)
        role: Role = request.user.role

        if role.name == "BISON" and service.user_bison.id != request.user.id:
            return JsonResponse(
                data={"message": "You do not have a service assigned with this id"},
                status=status.HTTP_403_FORBIDDEN
            )

        elif role.name == "CITIZEN" and service.user_citizen.id != request.user.id:
            return JsonResponse(
                data={"message": "You do not have a service assigned with this id"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer: ServiceSerializer = ServiceSerializer(service)
        return JsonResponse(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    except Service.DoesNotExist:
        return JsonResponse(
            data={"message": "Service does not exist"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )



@api_view(["POST"])
@permission_classes([IsAuthenticated, IsTokenValid, IsCitizen])
def get_service_price(request) -> JsonResponse:
    """

    :param request:
    :return:
    """
    try:
        start_checkpoint: Checkpoint = Checkpoint(request.data["origin_checkpoint"])
        end_checkpoint: Checkpoint = Checkpoint(request.data["destiny_checkpoint"])
        if request.data["type"] == "CARRIAGE":
            price: int = get_carriage_price(start_checkpoint, end_checkpoint)
        elif request.data["type"] == "PACKAGE":
            price: int = get_package_price(start_checkpoint, end_checkpoint, request.data["package"])
        else:
            raise TypeError("Invalid service type")

        return JsonResponse(
            data={"price": price},
            status=status.HTTP_200_OK
        )

    except KeyError:
        return JsonResponse(
            data={"message": "Missing required fields"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except ValueError as value:
        return JsonResponse(
            data={"message": f"{value} is not a valid Checkpoint"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except TypeError as msg:
        return JsonResponse(
            data={"message": f"{msg}"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsTokenValid, ~IsAdminUser])
def get_route(request) -> JsonResponse:
    """

    :param request:
    :return:
    """
    try:
        start_checkpoint: Checkpoint = Checkpoint(request.data["origin_checkpoint"])
        end_checkpoint: Checkpoint = Checkpoint(request.data["destiny_checkpoint"])
        route: list[str] = get_optimal_route(start_checkpoint, end_checkpoint)

        return JsonResponse(
            data={"route": route},
            status=status.HTTP_200_OK
        )

    except KeyError:
        return JsonResponse(
            data={"message": "Missing required fields"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except ValueError as value:
        return JsonResponse(
            data={"message": f"{value} is not a valid Checkpoint"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsTokenValid, IsBison])
def get_service_active(request) -> JsonResponse:
    """

    :param request:
    :return:
    """
    try:
        queryset = Service.objects.filter(user_bison=request.user.id, arrived__isnull=True).first()

        if not queryset:
            raise Http404("There is no active service")

        serializer = ServiceSerializer(queryset)

        return JsonResponse(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    except Http404 as e:
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_404_NOT_FOUND
        )

    except KeyError:
        return JsonResponse(
            data={"message": "Missing required fields"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except ValueError as value:
        return JsonResponse(
            data={"message": f"{value} is not a valid Checkpoint"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsTokenValid, IsCitizen])
def track_service(request, guide: int) -> JsonResponse:
    """

    :param request:
    :return:
    """
    try:
        queryset = Guide.objects.filter(guide_number=guide).first()

        if not queryset:
            raise Http404("Guide doesn't exist")

        serializer = GuideSerializer(queryset)
        return JsonResponse(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    except Http404 as e:
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_404_NOT_FOUND
        )

    except KeyError:
        return JsonResponse(
            data={"message": "Missing required fields"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except ValueError as value:
        return JsonResponse(
            data={"message": f"{value} is not a valid Checkpoint"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
