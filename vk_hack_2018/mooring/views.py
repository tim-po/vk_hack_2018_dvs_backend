import dateutil.parser
from django.http import JsonResponse, HttpResponse

import pytz

from rest_framework.views import APIView

from .models import MooringPlace, Reservation
from .serializers import MooringPlaceSerializer, ReservationSerializer


class MooringPlaceInfo(APIView):
    def serialize(self, places):
        serializer = MooringPlaceSerializer(places, many=True)
        json_data = JsonResponse(serializer.data, safe=False)
        return json_data

    def get(self, request):
        all_places = MooringPlace.objects.all()

        if request.GET == {}:
            return self.serialize(all_places)

        elif "time" in request.GET and "date" in request.GET:
            places = {}
            reserved = False

            time = request.GET["time"]
            date = request.GET["date"]

            date_time = dateutil.parser.parse(time + " " + date)

            for place in all_places:
                for reservation in place.reservations.all():

                    time_from = reservation.time_from
                    time_to = reservation.time_to

                    if time_from <= pytz.utc.localize(date_time) <= time_to:
                        reserved = True
                        break

                places[place.id] = reserved
            return JsonResponse(places)

    def post(self, request):
        time_start = request.POST["time_start"]
        data_start = request.POST["date_start"]

        time_finish = request.POST["time_finish"]
        data_finish = request.POST["date_finish"]

        boat_name = request.POST["boat_name"]

        mooring_id = int(request.POST["mooring_id"])

        date_time_start = dateutil.parser.parse(time_start + " " + data_start)
        date_time_finish = dateutil.parser.parse(time_finish + " " + data_finish)

        reservation = Reservation(
            time_from=pytz.utc.localize(date_time_start),
            time_to=pytz.utc.localize(date_time_finish),
            boat_name=boat_name
        )
        reservation.save()

        mooring_place = MooringPlace.objects.get(id=mooring_id)

        mooring_place.reservations.add(reservation)

        mooring_place.save()

        return HttpResponse(status=200)
