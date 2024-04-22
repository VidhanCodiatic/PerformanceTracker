from django.db import models

class PerformanceManager(models.Manager):
    def filter_by_min_roi(self, min_roi: float):
      return self.get_queryset().filter(profit__gte=min_roi)
