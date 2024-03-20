from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from ajax_select import make_ajax_field


class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True, label="Cuenta de Correo")
    profesion = forms.CharField(max_length=50, required=True)
    cursos = forms.ModelMultipleChoiceField(queryset=Curso.objects.all(), required=True, widget=forms.CheckboxSelectMultiple)
    #comision = forms.ModelChoiceField(queryset=Curso.objects.all(), required=True)  # Utiliza un campo de selección para la comisión
    comision = forms.IntegerField(required=True)
    
class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    comision = forms.IntegerField(required=True)


class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
    

class EntregableFormulario(forms.Form):
    
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    fechaDeEntrega = forms.DateField(required=True) 
    entregado = forms.BooleanField(required=True)

    

#class EstudianteForm(forms.ModelForm):
#    nombre = forms.CharField(max_length=50, required=True)
#    apellido = forms.CharField(max_length=50, required=True)
#    email = forms.EmailField(required=True, label="Cuenta de Correo")
#    cursos = forms.ModelMultipleChoiceField(queryset=Curso.objects.all(), required=True, widget=forms.CheckboxSelectMultiple)
#    comision = forms.ChoiceField(choices=[], required=True)  # Utiliza un campo de selección para la comisión
    
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['comision'].choices = [(curso.comision, curso.comision) for curso in Curso.objects.all()]


class EstudianteForm(forms.ModelForm):
    comision = forms.ModelChoiceField(queryset=None, required=True)  # Utiliza un campo de selección para la comisión

    class Meta:
        model = Estudiante  # Aquí se especifica el modelo Estudiante
        fields = ['nombre', 'apellido', 'email', 'cursos', 'comision']  # Selecciona los campos del modelo que deseas incluir en el formulario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comision'].queryset = Curso.objects.all()

