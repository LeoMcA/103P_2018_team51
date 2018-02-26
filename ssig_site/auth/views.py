from django.shortcuts import render, redirect
from django.conf import settings

from urllib.parse import urlencode
import requests


def start(request):
    state = 'ayylmao'
    request.session['state'] = state

    params = urlencode({'client_id': settings.UCLAPI_CLIENT_ID, 'state': state})

    url = settings.UCLAPI_URL + '/oauth/authorise?' + params
    return redirect(url)

def callback(request):
    # TODO: check state
    code = request.GET.get('code')

    token_params = {
        'client_id': settings.UCLAPI_CLIENT_ID,
        'code': code,
        'client_secret': settings.UCLAPI_CLIENT_SECRET
    }

    token_url = settings.UCLAPI_URL + '/oauth/token'
    token_req = requests.get(token_url, params=token_params)

    token_res = token_req.json()
    # TODO: check state

    user_params = {
        'token': token_res['token'],
        'client_secret': settings.UCLAPI_CLIENT_SECRET
    }

    user_url = settings.UCLAPI_URL + '/oauth/user/data'
    user_req = requests.get(user_url, params=user_params)

    user_res = user_req.json()
    # TODO: check state
    print(user_res)
