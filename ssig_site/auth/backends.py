from django.contrib.auth import get_user_model
from django.conf import settings

import requests

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

            User = get_user_model()
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
            return user

        return None

    def get_user(self, upi):
        User = get_user_model()
        try:
            return User.objects.get(pk=upi)
        except User.DoesNotExist:
            return None
