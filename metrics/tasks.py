from metrics.slow_iteration import slow_iteration
from PerformanceTracker.celery import app

@app.task
def slow_iteration_task():
  print("I am checking your stuff")
  return slow_iteration()
