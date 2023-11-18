from rest_framework import serializers

from .carriage_serializer import CarriageSerializer
from .guide_serializer import GuideSerializer
from .package_serializer import PackageSerializer
from ..models import Carriage, Package
from ..models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    carriage = serializers.SerializerMethodField()
    package = serializers.SerializerMethodField()
    guide = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            "id",
            "user_citizen",
            "user_bison",
            "type",
            "created",
            "arrived",
            "price",
            "origin_nation",
            "origin_checkpoint",
            "destiny_nation",
            "destiny_checkpoint",
            "route",
            "carriage",
            "package",
            "guide"
        ]

    def get_carriage(self, service: Service):
        try:
            carriage: Carriage = service.carriage
            if carriage:
                carriage_data = CarriageSerializer(carriage).data
                carriage_data.pop("service")
                return carriage_data
        except Carriage.DoesNotExist:
            return None

    def get_package(self, service: Service):
        try:
            package: Package = service.package
            if package:
                package_data = PackageSerializer(package).data
                package_data.pop("service")
                return package_data
        except Package.DoesNotExist:
            return None

    def get_guide(self, service: Service):
        guide: Package = service.guide
        if guide:
            guide_data = GuideSerializer(guide).data
            guide_data.pop("service")
            return guide_data

    def create(self, validated_data):
        service: Service = Service.objects.create(**validated_data)
        service.save()

        return service
