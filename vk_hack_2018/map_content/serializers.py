from rest_framework import serializers
from .models import Place


class PlaceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            "id",
            "name",
            "description",
            "category"
        )
