from django.utils.timezone import now

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def echo(request):
    if request.method == 'POST':
        username = request.user.username
        tstamp = now().strftime('%D | %T')
        text = request.data.get('text', '')
        message = """Echo: '%s' from %s (%s)""" % (text, username, tstamp)
        return Response(message, status.HTTP_201_CREATED)
    elif request.method == 'GET':
        return Response('Echo')
    
