from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from authentication.permissions.is_token_valid import IsTokenValid
from services.serializers.carriage_serializer import CarriageSerializer


# @api_view(["POST", "GET"])
# def create_get_carriage(request) -> JsonResponse:
#     """_summary_
#
#     Args:
#         request (_type_): _description_
#
#     Returns:
#         JsonResponse: _description_
#     """
#     if request.method == "POST":
#         serializer: CarriageSerializer = CarriageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return
#
#
#         return JsonResponse(
#             data={"message": "Heree"},
#             status=status.HTTP_200_OK
#         )




