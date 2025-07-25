from django.shortcuts import render,redirect
from .models import Estudio, Conocimiento, Empleo, idioma
from django.http import HttpResponse
from .forms import  ConocimientoForm, EstudioForm, EmpleoForm, IdiomaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView,TemplateView
from django.urls import reverse_lazy


def inicio(request):
    return render(request,'primer_app/inicio.html')


# def crear_estudio(request, name):
#     if name is not None:
#         nuevo_estudio = Estudio(
#             nombre=name,
#             institucion="Institución de " + name,
#             fecha_inicio="2023-01-01",
#             fecha_final=None,
#             descripcion="Descripción del estudio " + name,
#         )
#         nuevo_estudio.save()
#         return render(request, 'primer_app/crear_estudio.html', {'estudio': name})
    

# def crear_conocimiento(request):
#     if request.method == 'POST':
#         form = ConocimientoForm(request.POST)
#         if form.is_valid():
#             nuevo_conocimiento = Conocimiento(
#                 nombre=form.cleaned_data['nombre'],
#                 nivel=form.cleaned_data['nivel'],
#                 extra_comment=form.cleaned_data['extra_comment']
#             )
#             nuevo_conocimiento.save()
#             return redirect('inicio')
#     else:
#         form = ConocimientoForm()
#         return render(request, 'primer_app/crear_conocimiento.html', {'form': form})

    
# def conocimiento(request):
#     conocimientos = Conocimiento.objects.all()
#     return render(request, 'primer_app/buscar_conocimiento.html', {'conocimientos': conocimientos})


# def crear_estudio(request):
#     if request.method == 'POST':
#         form = EstudioForm(request.POST)
#         if form.is_valid():
#             nuevo_estudio = Estudio(
#                 nombre=form.cleaned_data['nombre'],
#                 institucion=form.cleaned_data['institucion'],
#                 fecha_inicio=form.cleaned_data['fecha_inicio'],
#                 fecha_final=form.cleaned_data['fecha_final'],
#                 descripcion=form.cleaned_data['descripcion']
#             )
#             nuevo_estudio.save()
#             return redirect('inicio')
#     else:
#         form = EstudioForm()
#         return render(request, 'primer_app/crear_estudio.html', {'form': form})

# def crear_empleo(request):
#     if request.method == 'POST':
#         form = EmpleoForm(request.POST)
#         if form.is_valid():
#             nuevo_empleo = Empleo(
#                 nombre=form.cleaned_data['nombre'],
#                 empresa=form.cleaned_data['empresa'],
#                 fecha_inicio=form.cleaned_data['fecha_inicio'],
#                 fecha_final=form.cleaned_data['fecha_final'],
#                 descripcion=form.cleaned_data['descripcion'],
#                 tecnologias_utilizadas=form.cleaned_data['tecnologias_utilizadas']
#             )
#             nuevo_empleo.save()
#             return redirect('inicio')
#     else:
#         form = EmpleoForm()
#         return render(request, 'primer_app/crear_empleo.html', {'form': form})
    
def buscar_conocimiento(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre','')
        conocimientos = Conocimiento.objects.filter(nombre__icontains=nombre)
        return render(request, 'primer_app/buscar_conocimiento.html', {'conocimientos': conocimientos, 'nombre': nombre})

    #Vistas basadas en clases

class InicioView(TemplateView):
    template_name = 'primer_app/inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleos'] = Empleo.objects.all()
        context['estudios'] = Estudio.objects.all()
        return context

##conocimiento
class conocimiento_delete(DeleteView):
    model = Conocimiento
    template_name = 'primer_app/conocimiento_delete.html'
    success_url = reverse_lazy('conocimiento_list')

class conocimiento_list(ListView):
    model = Conocimiento
    template_name = 'primer_app/conocimiento_list.html'
    context_object_name = 'conocimientos'

class conocimiento_create(CreateView):
    model = Conocimiento
    form_class = ConocimientoForm
    template_name = 'primer_app/conocimiento_create.html'
    success_url = reverse_lazy('conocimiento_list')

class conocimiento_update(UpdateView):
    model = Conocimiento
    form_class = ConocimientoForm
    template_name = 'primer_app/conocimiento_create.html'
    success_url = reverse_lazy('conocimiento_list')


##estudio
class estudio_delete(DeleteView):
    model = Estudio
    template_name = 'primer_app/estudio_delete.html'
    success_url = reverse_lazy('estudio_list')

class estudio_list(ListView):
    model = Estudio
    template_name = 'primer_app/estudio_list.html'
    context_object_name = 'estudios'

class estudio_create(CreateView):
    model = Estudio
    form_class = EstudioForm
    template_name = 'primer_app/estudio_create.html'
    success_url = reverse_lazy('estudio_list')

class estudio_update(UpdateView):
    model = Estudio
    form_class = EstudioForm
    template_name = 'primer_app/estudio_create.html'
    success_url = reverse_lazy('estudio_list')

##empleo
class empleo_list(ListView):
    model = Empleo
    template_name = 'primer_app/empleo_list.html'
    context_object_name = 'empleos'

class empleo_create(CreateView):
    model = Empleo
    form_class = EmpleoForm
    template_name = 'primer_app/empleo_create.html'
    success_url = reverse_lazy('empleo_list')

class empleo_update(UpdateView):
    model = Empleo
    form_class = EmpleoForm
    template_name = 'primer_app/empleo_create.html'
    success_url = reverse_lazy('empleo_list')

class empleo_delete(DeleteView):
    model = Empleo
    template_name = 'primer_app/empleo_delete.html'
    success_url = reverse_lazy('empleo_list')

class empleo_detail(DetailView):
    model = Empleo
    template_name = 'primer_app/empleo_detail.html'
    context_object_name = 'empleo'

###idioma
class idioma_list(ListView):
    model = idioma
    template_name = 'primer_app/idioma_list.html'
    context_object_name = 'idiomas'

class idioma_create(CreateView):
    model = idioma
    form_class = IdiomaForm
    template_name = 'primer_app/idioma_create.html'
    success_url = reverse_lazy('idioma_list')

class idioma_update(UpdateView):
    model = idioma
    form_class = IdiomaForm
    template_name = 'primer_app/crear_idioma.html'
    success_url = reverse_lazy('idioma_list')

class idioma_delete(DeleteView):
    model = idioma
    template_name = 'primer_app/idioma_delete.html'
    success_url = reverse_lazy('idioma_list')



