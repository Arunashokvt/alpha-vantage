from django.urls import path
from . import views

urlpatterns = [
    path('quotes', views.ExchangeView().as_view(), name='rate_change')
]