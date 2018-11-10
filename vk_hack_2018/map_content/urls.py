from django.conf.urls import url

from .views import PlaceInfo


urlpatterns = [
    url(r'$', PlaceInfo.as_view()),
]
