from django.contrib import messages
from django.shortcuts import redirect
from pprint import pprint
from social_core.exceptions import SocialAuthBaseException

from django.contrib import messages

def redirect_unauthorized_user(backend, user, response, *args, **kwargs):
    request = backend.strategy.request
    if not user:
        return redirect('/accounts/access-denied/')
