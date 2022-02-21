from django import views
from django.urls import path
from . import views

app_name='controle'

urlpatterns = [
    path('', views.Home, name='home')
]
