from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetAPIKeyView().as_view(), name='keys_get')
]