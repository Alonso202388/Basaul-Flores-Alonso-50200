from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('cursos/', cursos, name="cursos"),   
    path('curso_form/', cursoForm, name="curso_form"),

    path('entregables/', entregables, name="entregables"),
    #____________________________________________________ Profesores
    path('profesores/', profesores, name="profesores"),
    path('profesor_crear/', createProfesor, name="profesorCrear"),
    path('profesor_actualizar/<id_profesor>/', updateProfesor, name="profesorActualizar"),
    path('profesor_borrar/<id_profesor>/', deleteProfesor, name="profesorBorrar"),
    #____________________________________________________ Estudiantes
    path('estudiantes/', EstudianteList.as_view(), name="estudiantes"),
    path('estudiante_create/', EstudianteCreate.as_view(), name="estudiante_create"),
    path('estudiante_update/<int:pk>/', EstudianteUpdate.as_view(), name="estudiante_update"),
    path('estudiante_delete/<int:pk>/', EstudianteDelete.as_view(), name="estudiante_delete"),
    #____________________________________________________ login, logout, registro
    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),


    path('buscar/', buscar, name="buscar"),
    path('buscarCursos/', buscarCursos, name="buscarCursos"),
    path('autor/', autor, name="autor"),
]