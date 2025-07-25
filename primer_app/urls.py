
from django.contrib import admin
from django.urls import path
from .views import (inicio,buscar_conocimiento,
                    # crear_estudio,crear_conocimiento,conocimiento,crear_empleo,
                    InicioView,
                    estudio_list,empleo_list,conocimiento_list,idioma_list,
                    conocimiento_create,empleo_create,estudio_create,idioma_create,
                    empleo_detail,
                    conocimiento_update,empleo_update,estudio_update,idioma_update,
                    conocimiento_delete,empleo_delete,estudio_delete,idioma_delete)

urlpatterns = [
    # path('', inicio, name='inicio'),
    path('conocimiento/buscar', buscar_conocimiento, name='buscar-conocimiento'),
    # path('conocimiento/', conocimiento, name='conocimiento'),
    # # path('crear-conocimiento/', crear_conocimiento,name='crear-conocimiento'),
    # path('crear-estudio/',crear_estudio,name = 'crear-estudio'),
    # path('crear-empleo/',crear_empleo,name = 'crear-empleo'),


# urls con vistas basadas en clases
path('', InicioView.as_view(), name='inicio'),

path('lista-conocimientos/', conocimiento_list.as_view(), name='conocimiento_list'),
path('lista-empleos/', empleo_list.as_view(), name='empleo_list'),
path('lista-estudios/', estudio_list.as_view(), name='estudio_list'),
path('lista-idiomas/', idioma_list.as_view(), name='idioma_list'),

path('crear-conocimiento/', conocimiento_create.as_view(), name='conocimiento_create'),
path('crear-empleo/', empleo_create.as_view(), name='empleo_create'),
path('crear-estudio/', estudio_create.as_view(), name='estudio_create'),
path('crear-idioma/', idioma_create.as_view(), name='idioma_create'),

path('actualizar-conocimiento/<int:pk>/', conocimiento_update.as_view(), name='conocimiento_update'),
path('actualizar-empleo/<int:pk>/', empleo_update.as_view(), name='empleo_update'),
path('actualizar-estudio/<int:pk>/', estudio_update.as_view(), name='estudio_update'),
path('actualizar-idioma/<int:pk>/', idioma_update.as_view(), name='idioma_update'),

path('eliminar-conocimiento/<int:pk>/', conocimiento_delete.as_view(), name='conocimiento_delete'),
path('eliminar-empleo/<int:pk>/', empleo_delete.as_view(), name='empleo_delete'),
path('eliminar-estudio/<int:pk>/', estudio_delete.as_view(), name='estudio_delete'),    
path('eliminar-idioma/<int:pk>/', idioma_delete.as_view(), name='idioma_delete'),

path('detalle-empleo/<int:pk>/', empleo_detail.as_view(), name='empleo_detail'),

]

