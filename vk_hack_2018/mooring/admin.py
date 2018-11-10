from django.contrib import admin
from .models import *


class MooringPlaceAdmin(admin.ModelAdmin):
    filter_horizontal = ['reservations']


admin.site.register(MooringPlace, MooringPlaceAdmin)
admin.site.register(Reservation)
