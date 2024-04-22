import random
from decimal import Decimal
from metrics.constant import (MIN_ROI, ROI_LENGTH,
                        START_RANDOM_FACTOR, END_RANDOM_FACTOR)
from metrics.models import DailyPerformance

def random_revenue():
    # Filter queryset where ROI > 50%
    queryset = DailyPerformance.dp.filter_by_min_roi(MIN_ROI)[:ROI_LENGTH]

    # Print the length of the filtered queryset
    print("Length of the filtered queryset:", len(queryset))

    # Print the length of the filtered queryset multiplied by 2
    print("Length of the filtered queryset multiplied by 2:", len(queryset) * 2)

    # Iterate over the queryset and update revenue with a random factor
    for index, daily_performance in enumerate(queryset, start=1):
        print(f"Progress: {index}/{len(queryset)}", end="\r")

        random_factor = Decimal(random.uniform(START_RANDOM_FACTOR, END_RANDOM_FACTOR))
        new_revenue = daily_performance.revenue * random_factor
        daily_performance.revenue = new_revenue
        daily_performance.save()

    print("\nProcessing complete.")

if __name__ == "__main__":
    random_revenue()
