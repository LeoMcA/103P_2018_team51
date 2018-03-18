from django.db import models
from django.utils.timezone import now
from django.contrib.postgres.fields import JSONField


class Metric(models.Model):
    name = models.CharField(max_length=200)
    datetime = models.DateTimeField(default=now)
    increment = models.SmallIntegerField(default=1)
    data = JSONField(default=dict)
