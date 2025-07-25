from django import forms
from .models import idioma,Conocimiento,Empleo,Estudio

# class EstudioForm(forms.Form):
#     nombre = forms.CharField(label='Nombre del Estudio', max_length=100)
#     institucion = forms.CharField(label='Institución', max_length=100)
#     fecha_inicio = forms.DateField(label='Fecha de Inicio', widget=forms.SelectDateWidget(years=range(2000, 2030)))
#     fecha_final = forms.DateField(label='Fecha Final', required=False, widget=forms.SelectDateWidget(years=range(2000, 2030)))
#     descripcion = forms.CharField(label='Descripción', widget=forms.Textarea)


# class ConocimientoForm(forms.Form):
#     nombre = forms.CharField(label='Nombre del Conocimiento', max_length=100)
#     nivel = forms.ChoiceField(label='Nivel', choices=[
#         ('Básico', 'Básico'),
#         ('Intermedio', 'Intermedio'),
#         ('Avanzado', 'Avanzado'),
#         ('Experto', 'Experto')
#     ])
#     extra_comment = forms.CharField(label='Comentario Extra', required=False, widget=forms.Textarea)

# class EmpleoForm(forms.Form):
#     nombre = forms.CharField(label='Nombre del Empleo', max_length=100)
#     empresa = forms.CharField(label='Empresa', max_length=100)
#     fecha_inicio = forms.DateField(label='Fecha de Inicio', widget=forms.SelectDateWidget(years=range(2000, 2030)))
#     fecha_final = forms.DateField(label='Fecha Final', required=False, widget=forms.SelectDateWidget(years=range(2000, 2030)))
#     descripcion = forms.CharField(label='Descripción', widget=forms.Textarea)
#     tecnologias_utilizadas = forms.CharField(label='Tecnologías Utilizadas', max_length=200)


class IdiomaForm(forms.ModelForm):
    class Meta:
        model = idioma
        fields = ['nombre', 'nivel']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'nombre': 'Nombre',
            'nivel': 'Nivel'
        }

class ConocimientoForm(forms.ModelForm):
    class Meta:
        model = Conocimiento
        fields = ['nombre', 'nivel', 'extra_comment']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel': forms.Select(attrs={'class': 'form-control'}),
            'extra_comment': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'nombre': 'Nombre',
            'nivel': 'Nivel',
            'extra_comment': 'Comentario Extra'
        }
        
class EmpleoForm(forms.ModelForm):
    class Meta:
        model = Empleo
        fields = ['nombre', 'empresa', 'fecha_inicio', 'fecha_final', 'descripcion', 'tecnologias_utilizadas']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.SelectDateWidget(years=range(2000, 2030)),
            'fecha_final': forms.SelectDateWidget(years=range(2000, 2030)),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'tecnologias_utilizadas': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'nombre': 'Nombre',
            'empresa': 'Empresa',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_final': 'Fecha Final',
            'descripcion': 'Descripción',
            'tecnologias_utilizadas': 'Tecnologías Utilizadas'
        }

class EstudioForm(forms.ModelForm):
    class Meta:
        model = Estudio
        fields = ['nombre', 'institucion', 'fecha_inicio', 'fecha_final', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.SelectDateWidget(years=range(2000, 2030)),
            'fecha_final': forms.SelectDateWidget(years=range(2000, 2030)),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'nombre': 'Nombre',
            'institucion': 'Institución',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_final': 'Fecha Final',
            'descripcion': 'Descripción'
        }