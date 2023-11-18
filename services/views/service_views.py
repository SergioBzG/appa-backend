from django.http import JsonResponse
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from authentication.permissions.is_token_valid import IsTokenValid
from authentication.permissions.role_permissions import IsCitizen, IsBison

from ..helpers.get_service_price_and_route import get_service_price_and_route
from ..models import Service, Guide
from ..serializers.carriage_serializer import CarriageSerializer
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
        # set price and route to 0 and empty string
        request.data["price"] = 0
        request.data["route"] = ""
        service_serializer: ServiceSerializer = ServiceSerializer(data=request.data)
        if service_serializer.is_valid():
            service = service_serializer.save()
            # get price and route
            price, route = get_service_price_and_route(service=service)
            service.price = price
            service.route = route
            service.save(update_fields=["price", "route"])

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
        request.data["price"] = 0
        service_serializer: ServiceSerializer = ServiceSerializer(data=request.data)

        if service_serializer.is_valid():
            service = service_serializer.save()
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


@api_view(["PATCH", "GET"])
@permission_classes([IsAuthenticated, IsTokenValid, IsBison])
def update_get_service(request, service_id: int) -> JsonResponse:
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

        if request.method == "PATCH":
            guide: Guide = service.guide
            guide.current_nation = request.data["current_nation"]
            guide.current_checkpoint = request.data["current_checkpoint"]
            guide.save(update_fields=["current_nation", "current_checkpoint"])

            if guide.current_checkpoint == service.destiny_checkpoint:
                service.arrived = timezone.now()

            if service.type == "CARRIAGE" and "price" in request.data:
                service.price = request.data["price"]
                service.save(update_fields=["price"])

            serializer: ServiceSerializer = ServiceSerializer(service)
            data: dict = {"message": "Service updated successfully", "service": serializer.data}
            return JsonResponse(data=data, status=status.HTTP_200_OK)

        elif request.method == "GET":
            serializer: ServiceSerializer = ServiceSerializer(service)
            return JsonResponse(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

    except Service.DoesNotExist:
        return JsonResponse(
            data={"message": "Service does not exist"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except KeyError:
        return JsonResponse(
            data={"message": f"Missing required fields"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return JsonResponse(
            data={"error message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
