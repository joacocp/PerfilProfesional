
from django.contrib import admin
from django.urls import path
from .views import saludo_inicial, saludo_despedida


urlpatterns = [
    path('saludo-inicial/', saludo_inicial),
    path('saludo-despedida/',saludo_despedida),
]
