from django.conf.urls import url

from .views import PlaceInfo, DescriptionInfo


urlpatterns = [
    url(r'places/$', PlaceInfo.as_view()),
    url(r'^places/descriptions/(?P<pk>[0-9]+)/$', DescriptionInfo.as_view()),
]
