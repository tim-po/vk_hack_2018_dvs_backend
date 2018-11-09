from django.contrib import admin
from .models import *


class MooringPlaceAdmin(admin.ModelAdmin):
    filter_horizontal = ['time_table']


admin.site.register(MooringPlace, MooringPlaceAdmin)
admin.site.register(TimePeriod)
# Register your models here.
