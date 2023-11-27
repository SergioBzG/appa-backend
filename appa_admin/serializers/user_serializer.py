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

    def validate(self, attrs):
        role = Role.objects.get(pk=self.initial_data["role"])
        document = attrs.get("document")
        vehicle = attrs.get("vehicle")

        if role.name == 'BISON' and (document is None or vehicle is None):
            raise serializers.ValidationError("Document and Vehicle must not be null for BISON role.")

        return attrs

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.password = validated_data.get("password", instance.password)
        instance.save()
        return instance

    def create(self, validated_data):
        validated_data["role"] = Role.objects.get(pk=self.initial_data["role"])
        user: User = User.objects.create_user(**validated_data)
        user.save()
        return user
