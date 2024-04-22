from django.contrib import admin
from metrics.models import DailyPerformance, HourlyPerformance

admin.site.register(DailyPerformance)
admin.site.register(HourlyPerformance)
