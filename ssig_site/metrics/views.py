from django.shortcuts import render
from django.http import JsonResponse
from django.db.models.functions import Cast
from django.db.models.fields import DateField
from django.db.models import Sum, Q, Func

from . import models


def index(request):
    return render(request, 'metrics.html')


def total_users(request):
    metrics = list(models.Metric.objects
                    .filter(name='user_registration')
                    .annotate(total=Func(
                        Sum('increment'),
                        template='%(expressions)s OVER (ORDER BY %(order_by)s)',
                        order_by='datetime'
                    ))
                    # Reference: https://stackoverflow.com/a/43520109
                    .annotate(date=Cast('datetime', DateField()))
                    .values('date', 'total'))
    return JsonResponse(metrics, safe=False)
