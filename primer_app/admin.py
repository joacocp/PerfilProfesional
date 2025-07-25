from django.contrib import admin

# Register your models here.
from .models import Empleo, Estudio, Conocimiento

register_models = [Empleo, Estudio, Conocimiento]

admin.site.register(register_models)