from django.db import models

# Create your models here.
class Empleo(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField(null=True, blank=True)
    descripcion = models.TextField()
    tecnologias_utilizadas = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} en {self.empresa} ({self.fecha_inicio} - {self.fecha_final if self.fecha_final else 'Actualidad'})"

class Estudio(models.Model):
    nombre = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField(null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} en {self.institucion} ({self.fecha_inicio} - {self.fecha_final if self.fecha_final else 'Actualidad'})"
    
class Conocimiento(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50,choices=[
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
        ('Experto', 'Experto')
    ])
    extra_comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.nivel})"
    

class idioma(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50,choices=[
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
        ('Experto', 'Experto')
    ])
    
    def __str__(self):
        return f"{self.nombre} ({self.nivel})"