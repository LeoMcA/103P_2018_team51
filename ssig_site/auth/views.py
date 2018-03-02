from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login

from urllib.parse import urlencode


def start(request):
    state = 'ayylmao'
    request.session['state'] = state

    params = urlencode({'client_id': settings.UCLAPI_CLIENT_ID, 'state': state})

    url = settings.UCLAPI_URL + '/oauth/authorise?' + params
    return redirect(url)

def callback(request):
    # TODO: check state
    code = request.GET.get('code')
    user = authenticate(request, code=code)

    if user:
        login(request, user)

    return redirect('index')
