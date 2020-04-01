from django.urls import path
from drfapi.api.views import echo

urlpatterns = [
    path('echo', echo, name='echo')
]
