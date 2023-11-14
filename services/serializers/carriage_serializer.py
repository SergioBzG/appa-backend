from rest_framework.serializers import ModelSerializer

from ..models.carriage import Carriage


class CarriageSerializer(ModelSerializer):

    class Meta:
        model = Carriage
        fields = "__all__"


