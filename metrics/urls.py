from django.urls import path
from metrics.api import (DailyPerformanceListCreate, DailyPerformanceRetrieveUpdate, HourlyPerformanceListCreate, HourlyPerformanceRetrieveUpdate)

urlpatterns = [
    path('dailyperformance/', DailyPerformanceListCreate.as_view(), name='dailyperformance-list'),
    path('dailyperformance/<int:pk>/', DailyPerformanceRetrieveUpdate.as_view(), name='dailyperformance-detail'),
    path('hourlyperformance/', HourlyPerformanceListCreate.as_view(), name='hourlyperformance-list'),
    path('hourlyperformance/<int:pk>/', HourlyPerformanceRetrieveUpdate.as_view(), name='hourlyperformance-detail'),
]
