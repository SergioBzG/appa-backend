from rest_framework.serializers import ModelSerializer

from ..models.package import Package


class PackageSerializer(ModelSerializer):

    class Meta:
        model = Package
        fields = "__all__"