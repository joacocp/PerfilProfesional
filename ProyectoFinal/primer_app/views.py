from django.shortcuts import render

from django.http import HttpResponse


def saludo_inicial(request):
    return HttpResponse("¡Hola, mundo! Este es el saludo inicial de mi proyecto Django.")

def saludo_despedida(request):
    return HttpResponse("¡Hasta luego! Este es el mensaje de despedida de mi proyecto Django.")

def saludo_con_template(request):
    return render(request, 'primer_app/saludo_inicial.html')

def crear_estudio(request, name):
    return render(request, 'primer_app/crear_estudio.html', {'name': name})
    