from django.conf import settings

from .models import User
from ssig_site.metrics.models import Metric

import requests
from secrets import compare_digest


class UCL:
    def authenticate(self, request, code=None):
        if code:
            token_params = {
                'client_id': settings.UCLAPI_CLIENT_ID,
                'code': code,
                'client_secret': settings.UCLAPI_CLIENT_SECRET
            }

            token_url = settings.UCLAPI_URL + '/oauth/token'
            token_req = requests.get(token_url, params=token_params)

            token_res = token_req.json()
            token_state = token_res['state']
            if not compare_digest(token_state, request.session['state']):
                raise Exception

            user_params = {
                'token': token_res['token'],
                'client_secret': settings.UCLAPI_CLIENT_SECRET
            }

            user_url = settings.UCLAPI_URL + '/oauth/user/data'
            user_req = requests.get(user_url, params=user_params)

            user_res = user_req.json()

            try:
                user = User.objects.get(upi=user_res['upi'])
            except KeyError:
                return None
            except User.DoesNotExist:
                user = User.objects.create_user(
                    upi=user_res['upi'],
                    email=user_res['email'],
                    department=user_res['department'],
                    full_name=user_res['full_name'],
                    given_name=user_res['given_name']
                )
                metric = Metric(
                    name='user_registration',
                    data={
                        'ucl': True,
                        'department': user.department
                    }
                )
                metric.save()
            return user

        return None

    def get_user(self, upi):
        try:
            return User.objects.get(pk=upi)
        except User.DoesNotExist:
            return None
