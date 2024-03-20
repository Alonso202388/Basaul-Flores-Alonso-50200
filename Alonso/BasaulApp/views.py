from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

# Create your views here.
def autor(request):
    return render(request, "aplicacion/autor.html")

@login_required
def cursos(request):
    contexto = {'cursos': Curso.objects.all()}
    return render(request, "aplicacion/cursos.html", contexto)

# Create your views here.
def cursoForm(request):
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso_nombre = miForm.cleaned_data.get("nombre")
            curso_comision = miForm.cleaned_data.get("comision")
            curso = Curso(nombre=curso_nombre, comision=curso_comision)
            curso.save()
            return render(request, "aplicacion/home.html")

    else:    
        miForm = CursoForm()

    return render(request, "aplicacion/cursoForm.html", {"form": miForm })

# ________________________________________________________ Buscar  
@login_required
def buscar(request):
    return render(request, "aplicacion/buscar.html")

@login_required
def buscarCursos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {"cursos": cursos }
        return render(request, "aplicacion/cursos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

#________________________________________________________ Profesores
@login_required
def profesores(request):
    contexto = {'profesores': Profesor.objects.all()}
    return render(request, "aplicacion/profesores.html", contexto)

@login_required
def createProfesor(request):
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            prof_nombre = miForm.cleaned_data.get("nombre")
            prof_apellido = miForm.cleaned_data.get("apellido")
            prof_email = miForm.cleaned_data.get("email")
            prof_profesion = miForm.cleaned_data.get("profesion")
            curso = miForm.cleaned_data.get("curso")
            comision = miForm.cleaned_data.get("comision")
            profesor = Profesor(nombre=prof_nombre, apellido=prof_apellido,
                                email=prof_email, profesion=prof_profesion, curso=curso,
                                comision=comision)
            profesor.save()
            return redirect(reverse_lazy('profesores'))

    else:    
        miForm = ProfesorForm()

    return render(request, "aplicacion/profesorForm.html", {"form": miForm })  


@login_required
def updateProfesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            profesor.nombre = miForm.cleaned_data.get('nombre')
            profesor.apellido = miForm.cleaned_data.get('apellido')
            profesor.email = miForm.cleaned_data.get('email')
            profesor.profesion = miForm.cleaned_data.get('profesion') 
            profesor.save()
            return redirect(reverse_lazy('profesores'))   
    else:
        miForm = ProfesorForm(initial={
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
            'email': profesor.email,
            'profesion': profesor.profesion,
        })
    return render(request, "aplicacion/profesorForm.html", {'form': miForm})

@login_required
def deleteProfesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()
    return redirect(reverse_lazy('profesores'))

# ________________________________________________________ Login, Logout, Registracion

def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)

            #____ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #__________________________________________

            return render(request, "aplicacion/home.html")
        else:
            return redirect(reverse_lazy('login'))
        
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm })    

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:    
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm })  

#__________________________ Editar perfil de usuario
@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "aplicacion/home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": form }) 


#________________________________________________________ Avatar
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            # __________________________________
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___________ Hago una url de la imagen en request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/home.html")

    else:    
        form = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": form })  


#________________________________________________________ Entregable
@login_required
def entregables(request):
    context = {
        'estudiantes': Estudiante.objects.all(),
        'entregables': Entregable.objects.all()  
    }
    return render(request, "aplicacion/entregables.html", context)

@login_required
def entregableCrear(request):
    if request.method == "POST":
        form = EntregableFormulario(request.POST)
        if form.is_valid():
            # Crear una instancia de Entregable con los datos del formulario
            entregable = Entregable(
                nombre=form.cleaned_data['nombre'],
                fechaDeEntrega=form.cleaned_data['fechaDeEntrega'],
                entregado=form.cleaned_data['entregado'],
                estudiante_id=form.cleaned_data['estudiante']  
            )
            entregable.save()
            return render(request, "entregables.html", {"mensaje": "Entregable creado con éxito"})
    else:
        form = EntregableFormulario()
    
    return render(request, "aplicacion/entregable_formulario.html", {"form": form})


@login_required
def entregableActualizar(request, id_entregable):
    entregable = Entregable.objects.get(id=id_entregable)
    if request.method == "POST":
        miForm = EntregableFormulario(request.POST, instance=entregable)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('entregables'))  # Redirigir a la lista de entregables
    else:
        miForm = EntregableFormulario(instance=entregable)
    return render(request, "aplicacion/entregable_formulario.html", {'form': miForm})

@login_required
def entregableBorrar(request, id_entregable):
    entregable = Entregable.objects.get(id=id_entregable)
    entregable.delete()
    return redirect(reverse_lazy('entregables'))

#________________________________________________________ Estudiantes

@login_required
def estudiantes(request):
    contexto = {'estudiantes': Estudiante.objects.all()}
    return render(request, "aplicacion/estudiantes.html", contexto)


@login_required
def createEstudiante(request):
    if request.method == "POST":
        miForm = EstudianteForm(request.POST)
        if miForm.is_valid():
            estudiante = miForm.save(commit=False)  # Crea una instancia de Estudiante sin guardarla en la base de datos aún
            estu_nombre = miForm.cleaned_data.get("nombre")
            estu_apellido = miForm.cleaned_data.get("apellido")
            estu_email = miForm.cleaned_data.get("email")
            cursos = miForm.cleaned_data.get("cursos")
            comision = miForm.cleaned_data.get("comision")
            estudiante.nombre = estu_nombre
            estudiante.apellido = estu_apellido
            estudiante.email = estu_email
            estudiante.save()  # Ahora se guarda el estudiante en la base de datos

            # Asignar los cursos al estudiante
            estudiante.cursos.set(cursos)
            # Asignar la comisión al estudiante
            estudiante.comision = comision
            estudiante.save()
            return redirect(reverse_lazy('estudiantes'))

    else:    
        miForm = EstudianteForm()

    return render(request, "aplicacion/estudianteForm.html", {"form": miForm })

@login_required
def updateEstudiante(request, id_estudiante):
    estudiante = Estudiante.objects.get(id=id_estudiante)
    if request.method == "POST":
        miForm = EstudianteForm(request.POST)
        if miForm.is_valid():
            estudiante.nombre = miForm.cleaned_data.get('nombre')
            estudiante.apellido = miForm.cleaned_data.get('apellido')
            estudiante.email = miForm.cleaned_data.get('email')
            estudiante.save()
            return redirect(reverse_lazy('estudiantes'))   
    else:
        miForm = EstudianteForm(initial={
            'nombre': estudiante.nombre,
            'apellido': estudiante.apellido,
            'email': estudiante.email,
        })
    return render(request, "aplicacion/estudianteForm.html", {'form': miForm})

@login_required
def deleteEstudiante(request, id_estudiante):
    estudiante = Estudiante.objects.get(id=id_estudiante)
    estudiante.delete()
    return redirect(reverse_lazy('estudiantes'))


#$
from ajax_select import register, LookupChannel
from .models import Curso

@register('comisiones')
class ComisionLookup(LookupChannel):
    model = Curso

    def get_query(self, q, request):
        return self.model.objects.filter(nombre__icontains=q)

    def format_item_display(self, item):
        return f"{item.nombre} - {item.comision}"