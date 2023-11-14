from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .carriage_serializer import CarriageSerializer
from .package_serializer import PackageSerializer
from ..models.service import Service


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

    def create(self, validated_data):
        service: Service = Service.objects.create(**validated_data)
        service.save()

        return service
