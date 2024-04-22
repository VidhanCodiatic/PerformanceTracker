from django.core.management.base import BaseCommand
from metrics.random_revenue import random_revenue

class Command(BaseCommand):
    help = 'Generate random revenue for DailyPerformance objects'

    def handle(self, *args, **options):
        random_revenue()

        self.stdout.write(self.style.SUCCESS('Successfully generated random revenue'))


# To run this:
# python manage.py generate_random_revenue

