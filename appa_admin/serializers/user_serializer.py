from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models.user import User

class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "role",
            "name",
            "document",
            "email",
            "phone",
            "vehicle",
            "available",
            "password"
        ]