
from django.contrib import admin
from django.urls import path
from .views import saludo_inicial, saludo_despedida,saludo_con_template,crear_estudio


urlpatterns = [
    path('saludo-inicial/', saludo_inicial),
    path('saludo/', saludo_con_template),
    path('saludo-despedida/',saludo_despedida),
    path('crear-estudio/<str:name>/',crear_estudio),
]
