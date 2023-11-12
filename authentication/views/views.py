from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from appa_admin.serializers.user_serializer import UserSerializer
from authentication.models.role import Role

@api_view(["POST"])
def register_user(request) -> JsonResponse:
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        JsonResponse: _description_
    """
    try:
        role = Role.objects.get(name=request.data["role"])
        request.data["role"] = role.id
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
    
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Role.DoesNotExist:
        return JsonResponse(data={"message":f"{request.data["role"]} role does not exist."}, status=status.HTTP_400_BAD_REQUEST)