#Proyecto: A.B. GestionEstudiantes
#Nombre del Autor: Alonso Basaul Flores

#Descripción
AB GestionEstudiantes es una aplicación web desarrollada con Django que permite gestionar estudiantes, profesores, cursos y entregables, así como también proporciona funcionalidades de inicio de sesión, registro, perfil de usuario, y un panel de administración.

#Objetivo Funcional
El objetivo de GestionEstudiantes es proporcionar una plataforma integral para la gestión de información relacionada con estudiantes, profesores, cursos y entregables, facilitando la administración y organización de actividades educativas.

#Funcionalidades Principales
Gestión de Estudiantes: Agregar, editar y eliminar estudiantes.
Gestión de Profesores: Agregar, editar y eliminar profesores.
Gestión de Cursos: Agregar, editar y eliminar cursos.
Gestión de Entregables: Agregar, editar y eliminar entregables asociados a cursos.
Autenticación de Usuarios: Registro, inicio de sesión y cierre de sesión de usuarios.
Perfil de Usuario: Visualización y edición de información de perfil de usuario.
Panel de Administración: Acceso al panel de administración de Django para gestionar los datos del sistema.
Modelos

#La aplicación utiliza los siguientes modelos de Django:
Estudiante: Modelo para representar la información de los estudiantes.
Profesor: Modelo para representar la información de los profesores.
Curso: Modelo para representar la información de los cursos.
Entregable: Modelo para representar la información de los entregables asociados a los cursos.
Usuario: Modelo integrado de Django para la gestión de usuarios y autenticación.

#Acceso al Panel de Administración
El acceso al panel de administración de Django se realiza mediante el usuario administrador predeterminado. A continuación se proporcionan las credenciales de inicio de sesión:

Usuario: 50200
Contraseña: [50200]

#Instalación y Ejecución
Para ejecutar el proyecto localmente, sigue estos pasos:

Clona este repositorio en tu máquina local.
Instala los requisitos del proyecto utilizando pip install -r requirements.txt.
Realiza las migraciones de la base de datos con python manage.py migrate.
Crea un superusuario administrador con python manage.py createsuperuser y sigue las instrucciones.
Inicia el servidor de desarrollo con python manage.py runserver.
Accede a la aplicación desde tu navegador web en http://127.0.0.1:8000/.

¡Listo! Ahora puedes empezar a utilizar A.B. GestionEstudiantes.