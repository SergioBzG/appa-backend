from django.contrib.auth import authenticate
from rest_framework.serializers import Serializer
from rest_framework import serializers
from appa_admin.models.user import User


class UserLoginSerializer(Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user: User = authenticate(**data)

        if not user:
            raise serializers.ValidationError("Incorrect Credentials")

        return user
