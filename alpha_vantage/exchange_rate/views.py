import os
import json
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.permissions import HasAPIKey
from .models import Exchange
from .serializers import ExchangeSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
# Create your views here.

class ExchangeView(APIView):
    # setting permission
    permission_classes = [HasAPIKey]

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def dispatch(self, *args, **kwargs):
      return super(ExchangeView, self).dispatch(*args, **kwargs)
    
    def get(self, request):
        try:
            rate = Exchange.objects.first()
            serializer = ExchangeSerializer(rate)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e),status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            # fetch exchange rate from Alpha vantage API
            url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=%s' % os.environ.get('ALPHA_VANTAGE_API_KEY','demo')
            r = requests.get(url)
            data = r.json()
            return Response(data)
        except Exception as e:
            return Response(str(e),status.HTTP_500_INTERNAL_SERVER_ERROR)