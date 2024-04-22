from django.db import models
from decimal import Decimal
from metrics.managers import PerformanceManager

class Performance(models.Model): 
  cost = models.DecimalField(max_digits=10, decimal_places=2)
  revenue = models.DecimalField(max_digits=10, decimal_places=2)
  creation_date = models.DateTimeField(auto_now_add=True)
  profit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

  def save(self, *args, **kwargs):
    self.profit = self.revenue - self.cost
    super().save(*args, **kwargs)

  class Meta:
    abstract = True


class HourlyPerformance(Performance):
  datetime = models.DateTimeField(auto_now_add=True)
  hp = PerformanceManager()

class DailyPerformance(Performance):
  date = models.DateField(auto_now_add=True)
  dp = PerformanceManager()
