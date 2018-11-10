from .models import Photo, Event, News, TimePeriod

from rest_framework import serializers


class TimePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimePeriod
        fields = (
            'time_from',
            'time_to'
        )


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = 'image',


class EventSerializer(serializers.ModelSerializer):
    dates = TimePeriodSerializer()

    class Meta:
        model = Event
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = News
        fields = '__all__'
