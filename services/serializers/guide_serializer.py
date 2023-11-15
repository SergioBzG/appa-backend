from rest_framework.serializers import ModelSerializer
from ..models.guide import Guide


class GuideSerializer(ModelSerializer):

    class Meta:
        model = Guide
        fields = "__all__"
