import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alpha_vantage.settings')

app = Celery('alpha_vantage')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()
