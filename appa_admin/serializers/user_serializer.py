from rest_framework import serializers

from authentication.models import Role
from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.StringRelatedField()

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

    def create(self, validated_data):
        validated_data["role"] = Role.objects.get(pk=self.initial_data["role"])
        user: User = User.objects.create_user(**validated_data)
        user.save()
        return user
