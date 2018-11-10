from .models import TimePeriod, MooringPlace

from rest_framework import serializers


class TimePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimePeriod
        fields = (
            'time_from',
            'time_to'
        )


class MooringPlaceSerializer(serializers.ModelSerializer):
    time_table = TimePeriodSerializer(read_only=True, many=True)

    class Meta:
        model = MooringPlace
        fields = '__all__'
