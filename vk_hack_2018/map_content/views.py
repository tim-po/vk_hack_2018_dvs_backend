from django.http import JsonResponse

from rest_framework.views import APIView

from .models import Place
from .serializers import PlaceSerializer


class PlaceInfo(APIView):
    def get(self, request):
        all_places = Place.objects.all()

        serializer = PlaceSerializer(all_places, many=True)
        json_data = JsonResponse(serializer.data, safe=False)

        return json_data
