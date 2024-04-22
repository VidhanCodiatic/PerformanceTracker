from rest_framework import generics
from metrics.models import DailyPerformance, HourlyPerformance
from metrics.serializers import DailyPerformanceSerializer, HourlyPerformanceSerializer

class DailyPerformanceListCreate(generics.ListCreateAPIView):
    queryset = DailyPerformance.dp.all()
    serializer_class = DailyPerformanceSerializer

class DailyPerformanceRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = DailyPerformance.dp.all()
    serializer_class = DailyPerformanceSerializer

class HourlyPerformanceListCreate(generics.ListCreateAPIView):
    queryset = HourlyPerformance.hp.all()
    serializer_class = HourlyPerformanceSerializer

class HourlyPerformanceRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = HourlyPerformance.hp.all()
    serializer_class = HourlyPerformanceSerializer
