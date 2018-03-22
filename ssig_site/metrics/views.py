from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db.models.functions import Trunc
from django.db.models import Sum, Func
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from . import models


def user_passes_test(test_func):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator


def staff_check(user):
    return user.is_staff


@user_passes_test(staff_check)
def index(request):
    return render(request, 'metrics.html')


@user_passes_test(staff_check)
def total_users(request):
    metrics = list(
        models.Metric.objects
        .filter(name='user_registration')
        .annotate(total=Func(
            Sum('increment'),
            template='%(expressions)s OVER (ORDER BY %(order_by)s)',
            order_by='datetime'
        ))
        # Reference: https://stackoverflow.com/a/43520109
        .annotate(date=Trunc('datetime', 'second'))
        .values('date', 'total')
    )
    return JsonResponse(metrics, safe=False)


@user_passes_test(staff_check)
def new_users(request, period):
    valid_periods = ('year', 'quarter', 'month', 'week', 'day')
    if period in valid_periods:
        metrics = list(
            models.Metric.objects
            .filter(name='user_registration')
            .annotate(date=Trunc('datetime', period))
            .values('date')
            .annotate(total=Sum('increment'))
            .values('date', 'total')
        )
        return JsonResponse(metrics, safe=False)
    else:
        return HttpResponse(status=404)


@user_passes_test(staff_check)
def events(request):
    registration_metrics = list(
        models.Metric.objects
        .filter(name='event_registration')
        .annotate(date=Trunc('datetime', 'week'))
        .values('date')
        .annotate(total=Sum('increment'))
        .values('date', 'total')
    )
    attendance_metrics = list(
        models.Metric.objects
        .filter(name='event_attendance')
        .annotate(date=Trunc('datetime', 'week'))
        .values('date')
        .annotate(total=Sum('increment'))
        .values('date', 'total')
    )
    return JsonResponse([registration_metrics, attendance_metrics], safe=False)
