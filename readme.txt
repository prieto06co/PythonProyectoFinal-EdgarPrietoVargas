BackEnd Django - Proyecto Final - Tienda de componentes de computadora

Autor: Edgar Armando Prieto Vargas
Fecha: 26/12/2024
Versión: 20241226

Estructura del proyecto:

miSitio/
│
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── myapp/
│   │       ├── acerca-de-nosotros.html
│   │       ├── base.html
│   │       ├── colaborador-detalle
│   │       ├── colaboradores.html
│   │       ├── componente-detalle.html
│   │       ├── componentes.html
│   │       ├── index.html
│   │       ├── perfil-usuario.html
│   │       ├── sede-detalle.html
│   │       ├── sedes.html
│   │       ├── forms/
│   │       │   ├── cambiar-clave-usuario.html
│   │       │   ├── colaborador-formulario.html
│   │       │   ├── componente-formulario.html
│   │       │   ├── editar-perfil.html
│   │       │   ├── logueo.html
│   │       │   ├── registro.html
│   │       │   └── sede-formulario.html
│   │       ├── deletes/
│   │       │   ├── colaborador-eliminar.html
│   │       │   ├── componente-eliminar.html
│   │       │   └── sede-eliminar.html
│   │       ├── updates/
│   │       │   ├── colaborador-editar.html
│   │       │   ├── componente-editar.html
│   │       │   └── sede-editar.html
│   │       └── updates/
│   │         └── promocion-componente.html
│   │
│   └── urls.py
│
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   ├── templates/
│   │   └── app_mensajeria/
│   │       ├── enviar-mensaje.html
│   │       └── mostrar-mensajes.html
│   │         
│   └── urls.py
│    
│
├── db.sqlite3
├── manage.py
└── readme.txt

# My Django App

## Cómo Probar el Proyecto
1. Clonar el repositorio:
   ```bash
   git clone <link-del-repositorio>
   cd miSitio
2. Instalar paquete Django:
	pip install django
3. Ejecutar Migraciones y creación DB
	python manage.py makemigrations
	python manage.py migrate
4. Ejecutar Servidor:
	python manage.py runserver

Información de SuperUsuario:
User: coder
Pass: coder2024

Funcionalidades
Home: Página de inicio (http://127.0.0.1:8000/).
Componentes: Pagina con listado de Componentes (http://127.0.0.1:8000/componentes/).
Colaboradores: Pagina con listado de Colaboradores (http://127.0.0.1:8000/colaboradores/).
Sedes: Pagina con listado de Sedes (http://127.0.0.1:8000/sedes/).
Acerca de: Pagina con un breve resumen de la empresa(http://127.0.0.1:8000/acerca_de_nosotros/).

Agregar Componentes: Formulario para agregar Componentes (http://127.0.0.1:8000/componente-formulario/).
Agregar Colaboradores: Formulario para agregar Colaboradores (http://127.0.0.1:8000/colaborador-formulario/).
Agregar Sedes: Formulario para agregar Sedes (http://127.0.0.1:8000/sede-formulario/).

Editar Componentes: Formulario para editar Componentes(http://127.0.0.1:8000/componente-editar/<int:pk>).
Editar Colaboradores: Formulario para editar Colaboradores: (http://127.0.0.1:8000/colaborador-editar/<int:pk>).
Editar Sedes: Formulario para editar Sedes: (http://127.0.0.1:8000/sede-editar/<int:pk>).

Detalle Componentes: Pagina con detalle Componente(http://127.0.0.1:8000/componente-detalle/<int:pk>).
Detalle Colaboradores: Pagina con detalle Colaborador: (http://127.0.0.1:8000/colaborador-detalle/<int:pk>).
Detalle Sedes: Pagina con detalle Sede: (http://127.0.0.1:8000/sede-detalle/<int:pk>).

Editar Componentes: Pagina para eliminar Componentes(http://127.0.0.1:8000/componente-eliminar/<int:pk>).
Editar Colaboradores: Pagina para eliminar Colaboradores: (http://127.0.0.1:8000/colaborador-eliminar//<int:pk>).
Editar Sedes: Pagina para eliminar Sedes: (http://127.0.0.1:8000/sede-eliminar/<int:pk>).

Perfil de Usuario: Pagina con información de usuario logueado (http://127.0.0.1:8000/perfil-usuario/).
Editar perfil de Usuario: Pagina para editar información de usuario logueado (http://127.0.0.1:8000/editar-perfil/).
Cambiar contraseña de Usuario: Pagina para cambiar contraseña de usuario logueado (http://127.0.0.1:8000/cambiar-clave-usuario/).

Enviar Mensaje: Pagina para enviar mensajes entre usuarios(http://127.0.0.1:8000/mensajes/enviar-mensaje).
Mostrar Mensajes: Pagina para mostrar mensajes de usuario logueado(http://127.0.0.1:8000/mensajes/mostrar-mensajes).


