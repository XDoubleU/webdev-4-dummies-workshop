from django.http import HttpResponse
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from mollie.api.client import Client

from accounts.models import CustomUser
from albums.models import Album


class MolliePaymentView(APIView):
  def post(self, request, format=None):
    id = request.POST.get('id')
    
    if id is None:
      return Response(status=status.HTTP_400_BAD_REQUEST)
    
    mollie_client = Client()
    mollie_client.set_api_key(settings.MOLLIE_API_KEY)

    payment = mollie_client.payments.get(id)
    if payment.is_paid():
      user = CustomUser.objects.get(id=payment.metadata['userid'])
      album = Album.objects.get(id=payment.metadata['albumid'])
      user.albums.add(album)
    
    return HttpResponse(status=status.HTTP_200_OK)