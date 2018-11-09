from django.conf.urls import url

from .views import EventsInfo, NewsInfo


urlpatterns = [
    url(r'events/$', EventsInfo.as_view()),
    url(r'news/$', NewsInfo.as_view())
]
