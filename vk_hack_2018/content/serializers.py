from .models import Photo, Event, News
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            "image"
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "description",
            "date",
            "photo",
            "link"
        )


class NewsSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = News
        fields = (
            "id",
            "content",
            "date",
            "photos"
        )
