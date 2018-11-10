from django.conf.urls import url

from .views import MooringPlaceInfo


urlpatterns = [
    url(r'$', MooringPlaceInfo.as_view())
]
