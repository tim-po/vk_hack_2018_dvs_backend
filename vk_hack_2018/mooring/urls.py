from django.conf.urls import url

from .views import MooringPlaceInfo


urlpatterns = [
    url(r'mooring_places/$', MooringPlaceInfo.as_view())
]
