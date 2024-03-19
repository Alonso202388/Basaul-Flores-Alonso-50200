from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.conf import settings

from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profesion = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Create your models here.
#class Curso(models.Model):
#    nombre = models.CharField(max_length=50)
#    comision = models.IntegerField()

#    def __str__(self):
#        return f"{self.nombre}"

#class Estudiante(models.Model):
#    nombre = models.CharField(max_length=50)
#    apellido = models.CharField(max_length=50)
#    email = models.EmailField()
 #   
#    class Meta:
#        verbose_name = "Estudiante"
#        verbose_name_plural = "Estudiantes"
#        ordering = ['nombre']    

#    def __str__(self):
#        return f"{self.apellido}, {self.nombre}"

#class Profesor(models.Model):
#    nombre = models.CharField(max_length=50)
#    apellido = models.CharField(max_length=50)
#    email = models.EmailField()
#    profesion = models.CharField(max_length=50)

#    class Meta:
#        verbose_name = "Profesor"
#        verbose_name_plural = "Profesores"
#        ordering = ['nombre']

#    def __str__(self):
#        return f"{self.apellido}, {self.nombre}"
    

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.estudiante:  # Verificar si el estudiante no es None
            return f'{self.nombre} {self.estudiante.nombre}'
        else:
            return f'{self.nombre} (sin estudiante)'


    #def __str__(self):
    #    return f'{self.nombre} {self.estudiante}'


   

    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}" 