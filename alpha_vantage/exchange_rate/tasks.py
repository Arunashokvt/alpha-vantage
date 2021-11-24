import os
import requests
from celery import shared_task
from .serializers import ExchangeSerializer


@shared_task()
def save_exchange_rate():
    """
    Saves latest exchange rate
    """
    try:
        print("Celery fetching exchange rate..")
        url = 'https://www.alphavantage.co/' \
              'query?function=CURRENCY_EXCHANGE_RATE&from_currency=' \
              'BTC&to_currency=USD&apikey=%s' % os.environ.get(
                'ALPHA_VANTAGE_API_KEY', 'demo')
        r = requests.get(url)
        data = {
            'from_currency': r.json()['Realtime Currency Exchange Rate']
            ['1. From_Currency Code'],
            'from_currency_name': r.json()['Realtime Currency Exchange Rate']
            ['2. From_Currency Name'],
            'to_currency': r.json()['Realtime Currency Exchange Rate']
            ['3. To_Currency Code'],
            'to_currency_name': r.json()['Realtime Currency Exchange Rate']
            ['4. To_Currency Name'],
            'exchange_rate': r.json()['Realtime Currency Exchange Rate']
            ['5. Exchange Rate'],
            'las_refreshed': r.json()['Realtime Currency Exchange Rate']
            ['6. Last Refreshed'],
            'time_zone': r.json()['Realtime Currency Exchange Rate']
            ['7. Time Zone'],
            'bid_price': r.json()['Realtime Currency Exchange Rate']
            ['8. Bid Price'],
            'ask_price': r.json()['Realtime Currency Exchange Rate']
            ['9. Ask Price'],
        }
        serializer = ExchangeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
    except Exception as e:
        print("Failed to fetch exchange rate | Error :%s" % str(e))
