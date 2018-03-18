from django.shortcuts import render
from django.http import JsonResponse
from django.db.models.functions import Cast, Trunc
from django.db.models import Sum, Func

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
                    .annotate(date=Trunc('datetime', 'second'))
                    .values('date', 'total'))
    return JsonResponse(metrics, safe=False)


def new_users(request, period):
    metrics = list(models.Metric.objects
                    .filter(name='user_registration')
                    .annotate(date=Trunc('datetime', period))
                    .values('date')
                    .annotate(total=Sum('increment'))
                    .values('date', 'total'))
    return JsonResponse(metrics, safe=False)
