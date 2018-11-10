from django.http import JsonResponse

from rest_framework.views import APIView

from .models import MooringPlace
from .serializers import MooringPlaceSerializer


class MooringPlaceInfo(APIView):
    def get(self, request):
        all_places = MooringPlace.objects.all()

        serializer = MooringPlaceSerializer(all_places, many=True)
        json_data = JsonResponse(serializer.data, safe=False)

        return json_data

