from django.shortcuts import render

from . import models


def index(request):
    return render(request, 'base.html')

def events(request):
    events = models.Event.objects.all()
    return render(request, 'events.html', { 'events': events })

def event(request, id):
    event = models.Event.objects.get(id=id)
    return render(request, 'event.html', { 'event': event })
