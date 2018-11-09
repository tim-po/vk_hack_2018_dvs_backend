from django.http import JsonResponse

from rest_framework.views import APIView

from .models import Photo, Event, News
from .serializers import PhotoSerializer, EventSerializer, NewsSerializer


class EventsInfo(APIView):
    def get(self, request):
        last_ten_events = News.objects.all().order_by('-id')[:10]

        serializer = EventSerializer(reversed(last_ten_events), many=True)
        json_data = JsonResponse(serializer.data, safe=False)

        return json_data


class NewsInfo(APIView):
    def get(self, request):
        last_ten_news = News.objects.all().order_by('-id')[:10]

        serializer = NewsSerializer(reversed(last_ten_news), many=True)

        json_data = JsonResponse(serializer.data, safe=False)

        return json_data
