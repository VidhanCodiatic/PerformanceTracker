import time
from metrics.constant import LIMIT
from metrics.models import DailyPerformance

def slow_iteration():
    queryset = DailyPerformance.dp.all()[:LIMIT]
    for index, daily_performance in enumerate(queryset, start=1):
        time.sleep(60)
        print(f"Processed {index} out of {len(queryset)}")
    print('Task is completed')
