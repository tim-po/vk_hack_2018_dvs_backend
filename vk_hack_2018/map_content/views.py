from .models import Place, HtmlDescription
from .serializers import PlaceSerializer

from django.http import JsonResponse, HttpResponse
from django.http import Http404

from rest_framework.views import APIView


class PlaceInfo(APIView):
    def get(self, request):
        all_places = Place.objects.all()

        serializer = PlaceSerializer(all_places, many=True)
        json_data = JsonResponse(serializer.data, safe=False)

        return json_data


class DescriptionInfo(APIView):
    def get_object(self, pk):
        try:
            return HtmlDescription.objects.get(pk=pk)
        except HtmlDescription.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            description = self.get_object(pk)
        except Http404:
            return HttpResponse(status=404)

        return HttpResponse(description.html_code)
