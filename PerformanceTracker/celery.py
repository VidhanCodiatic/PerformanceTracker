
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PerformanceTracker.settings')

app = Celery('PerformanceTracker', include=['metrics.tasks'])
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "run-slow-iteration-once-in-every-day": {
        "task": "metrics.tasks.slow_iteration_task",
        "schedule": crontab(hour=10, minute=00),
    }
}
