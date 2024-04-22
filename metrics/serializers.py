from rest_framework import serializers
from metrics.models import DailyPerformance, HourlyPerformance

class DailyPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPerformance
        fields = '__all__'

class HourlyPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HourlyPerformance
        fields = '__all__'
