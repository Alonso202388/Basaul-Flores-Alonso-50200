from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

import ajax_select
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from ajax_select import urls as ajax_select_urls

urlpatterns = [
    path('', home, name="home"),
    path('cursos/', cursos, name="cursos"),   
    path('curso_form/', cursoForm, name="curso_form"),
    path('ajax_select/', include(ajax_select.urls)),
    
    #____________________________________________________ Entregables
    path('entregables/', entregables, name="entregables"),
    path('entregable_crear/', entregableCrear, name="entregableCrear"),
    path('entregable_actualizar/<id_entregable>/', entregableActualizar, name="entregableActualizar"),
    path('entregable_borrar/<id_entregable>/', entregableBorrar, name="entregableBorrar"),
        

    #____________________________________________________ Profesores
    path('profesores/', profesores, name="profesores"),
    path('profesor_crear/', createProfesor, name="profesorCrear"),
    path('profesor_actualizar/<id_profesor>/', updateProfesor, name="profesorActualizar"),
    path('profesor_borrar/<id_profesor>/', deleteProfesor, name="profesorBorrar"),
  
    #____________________________________________________ login, logout, registro
    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

     #____________________________________________________ Buscar
    path('buscar/', buscar, name="buscar"),
    path('buscarCursos/', buscarCursos, name="buscarCursos"),
    path('autor/', autor, name="autor"),
    
    
     #____________________________________________________ Estudiantes
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('estudiante_crear/', createEstudiante, name="estudianteCrear"),
    path('estudiante_actualizar/<id_estudiante>/', updateEstudiante, name="estudianteActualizar"),
    path('estudiante_borrar/<id_estudiante>/', deleteEstudiante, name="estudianteBorrar"),
 
]