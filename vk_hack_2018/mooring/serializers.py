from .models import Reservation, MooringPlace

from rest_framework import serializers


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'boat_name',
            'time_from',
            'time_to'
        )


class MooringPlaceSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(read_only=True, many=True)

    class Meta:
        model = MooringPlace
        fields = '__all__'
