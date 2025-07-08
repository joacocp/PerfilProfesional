from django.shortcuts import render,redirect
from .models import Estudio, Conocimiento, Empleo
from django.http import HttpResponse
from .forms import  ConocimientoForm, EstudioForm, EmpleoForm


def inicio(request):
    return render(request,'primer_app/inicio.html')

def saludo_inicial(request):
    return HttpResponse("¡Hola, mundo! Este es el saludo inicial de mi proyecto Django.")

def saludo_con_template(request):
    return render(request, 'primer_app/saludo_inicial.html')

def crear_estudio(request, name):
    if name is not None:
        nuevo_estudio = Estudio(
            nombre=name,
            institucion="Institución de " + name,
            fecha_inicio="2023-01-01",
            fecha_final=None,
            descripcion="Descripción del estudio " + name,
        )
        nuevo_estudio.save()
        return render(request, 'primer_app/crear_estudio.html', {'estudio': name})
    

def crear_conocimiento(request):
    if request.method == 'POST':
        form = ConocimientoForm(request.POST)
        if form.is_valid():
            nuevo_conocimiento = Conocimiento(
                nombre=form.cleaned_data['nombre'],
                nivel=form.cleaned_data['nivel'],
                extra_comment=form.cleaned_data['extra_comment']
            )
            nuevo_conocimiento.save()
            return redirect('inicio')
    else:
        form = ConocimientoForm()
        return render(request, 'primer_app/crear_conocimiento.html', {'form': form})

def buscar_conocimiento(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre','')
        conocimientos = Conocimiento.objects.filter(nombre__icontains=nombre)
        return render(request, 'primer_app/buscar_conocimiento.html', {'conocimientos': conocimientos, 'nombre': nombre})
    
def conocimiento(request):
    conocimientos = Conocimiento.objects.all()
    return render(request, 'primer_app/buscar_conocimiento.html', {'conocimientos': conocimientos})


def crear_estudio(request):
    if request.method == 'POST':
        form = EstudioForm(request.POST)
        if form.is_valid():
            nuevo_estudio = Estudio(
                nombre=form.cleaned_data['nombre'],
                institucion=form.cleaned_data['institucion'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                fecha_final=form.cleaned_data['fecha_final'],
                descripcion=form.cleaned_data['descripcion']
            )
            nuevo_estudio.save()
            return redirect('inicio')
    else:
        form = EstudioForm()
        return render(request, 'primer_app/crear_estudio.html', {'form': form})

def crear_empleo(request):
    if request.method == 'POST':
        form = EmpleoForm(request.POST)
        if form.is_valid():
            nuevo_empleo = Empleo(
                nombre=form.cleaned_data['nombre'],
                empresa=form.cleaned_data['empresa'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                fecha_final=form.cleaned_data['fecha_final'],
                descripcion=form.cleaned_data['descripcion'],
                tecnologias_utilizadas=form.cleaned_data['tecnologias_utilizadas']
            )
            nuevo_empleo.save()
            return redirect('inicio')
    else:
        form = EmpleoForm()
        return render(request, 'primer_app/crear_empleo.html', {'form': form})