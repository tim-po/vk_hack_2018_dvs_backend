from django.http import JsonResponse

from rest_framework.views import APIView

from .models import Event, News
from .serializers import EventSerializer, NewsSerializer


class EventsInfo(APIView):
    def get(self, request):
        last_ten_events = Event.objects.all().order_by('-id')[:10]

        serializer = EventSerializer(reversed(last_ten_events), many=True)
        serializer_data = serializer.data

        for i, event in enumerate(serializer_data):
            serializer_data[i]["dates"]["time_from"] = event["dates"]["time_from"].replace("T", " ").replace("Z", "")
            serializer_data[i]["dates"]["time_to"] = event["dates"]["time_to"].replace("T", " ").replace("Z", "")

        json_data = JsonResponse(serializer_data, safe=False)

        return json_data


class NewsInfo(APIView):
    def get(self, request):
        last_ten_news = News.objects.all().order_by('-id')[:10]

        serializer = NewsSerializer(reversed(last_ten_news), many=True)

        serializer_data = serializer.data

        for i, news in enumerate(serializer_data):
            serializer_data[i]["date"] = news["date"].replace("T", " ").replace("Z", "")

        json_data = JsonResponse(serializer_data, safe=False)

        return json_data
