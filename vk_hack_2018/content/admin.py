from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'dates']
    list_display_link = ['__str__', 'dates']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'date']
    filter_horizontal = ['photos']
    list_filter = ['date']


admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(TimePeriod)
admin.site.register(Photo)
