
from django.contrib import admin
from django.urls import path
from .views import crear_estudio,inicio,crear_conocimiento,buscar_conocimiento,conocimiento,crear_empleo


urlpatterns = [
    path('', inicio, name='inicio'),
    path('conocimiento/buscar', buscar_conocimiento, name='buscar-conocimiento'),
    path('conocimiento/', conocimiento, name='conocimiento'),
    path('crear-conocimiento/', crear_conocimiento,name='crear-conocimiento'),
    path('crear-estudio/',crear_estudio,name = 'crear-estudio'),
    path('crear-empleo/',crear_empleo,name = 'crear-empleo'),

]
