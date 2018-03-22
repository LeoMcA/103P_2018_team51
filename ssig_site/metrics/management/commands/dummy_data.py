from django.core.management.base import BaseCommand, CommandError
from autofixture import generators, AutoFixture
from datetime import datetime
from ssig_site.metrics.models import Metric


class Command(BaseCommand):
    def handle(self, *args, **options):

        Metric.objects.all().delete()

        AutoFixture(Metric, field_values = {
            'name': generators.StaticGenerator('user_registration'),
            'datetime': generators.DateTimeGenerator(min_date=datetime(2018, 1, 1), max_date=datetime(2018, 4, 24)),
            'increment': generators.ChoicesGenerator(values=(-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
        }).create(160)

        AutoFixture(Metric, field_values = {
            'name': generators.StaticGenerator('event_registration'),
            'datetime': generators.DateGenerator(min_date=datetime(2018, 1, 1), max_date=datetime(2018, 4, 24)),
            'increment': generators.ChoicesGenerator(values=(2,))
        }).create(int(114 * 3))

        AutoFixture(Metric, field_values = {
            'name': generators.StaticGenerator('event_attendance'),
            'datetime': generators.DateGenerator(min_date=datetime(2018, 1, 1), max_date=datetime(2018, 4, 24)),
            'increment': generators.ChoicesGenerator(values=(1,))
        }).create(int(114 * 3))
