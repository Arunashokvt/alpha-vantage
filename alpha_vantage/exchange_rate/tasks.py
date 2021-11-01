from celery.task.schedules import crontab
from celery.decorators import periodic_task
from exchange_rate.serializers import ExchangeSerializer
@periodic_task(
    run_every=(crontab(hour='*/1')),
    name="save_exchange_rate",
    ignore_result=True
)
def save_exchange_rate():
    """
    Saves latest exchange rate
    """
    try:
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=%s' % os.environ.get('ALPHA_VANTAGE_API_KEY','demo')
        r = requests.get(url)
        data = r.json()
        serializer = ExchangeSerializer(data=data)
        serializer.save()
    except Exception as e:
        pass