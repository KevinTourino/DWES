#  Arcade Store
# <img width="1254" height="1254" alt="portada (2)" src="https://github.com/user-attachments/assets/c6bcb810-ffb0-4043-8484-1ac0afae94df" />
Aplicación web para la gestión personal de colecciones de videojuegos. Permite a los usuarios registrar, organizar y realizar el seguimiento de los videojuegos que poseen, controlando su progreso, plataformas y estado de completado.

##  Descripción

Arcade Store es una plataforma diseñada para ayudar a los aficionados a los videojuegos a gestionar su biblioteca personal de forma sencilla y centralizada.

Los usuarios pueden:

- Registrar videojuegos en su colección.
- Consultar información detallada de cada título.
- Gestionar el estado de progreso de los juegos.
- Asociar juegos a diferentes plataformas.
- Mantener un seguimiento de logros y completado.
- Buscar videojuegos mediante una API externa.
- Administrar su propia biblioteca de forma segura mediante autenticación.

##  Tecnologías utilizadas

### Frontend
- React
- React Router
- Axios / Fetch API
- HTML5
- CSS3
- JavaScript

### Backend
- Django
- Django REST Framework
- API REST

### Base de datos
- SQLite

##  Arquitectura

El proyecto sigue una arquitectura cliente-servidor:

```text
React (Frontend)
       │
       ▼
API REST (Django REST Framework)
       │
       ▼
Base de Datos (SQLite)
```

### Flujo principal

1. El usuario accede a la aplicación.
2. Se autentica mediante login o registro.
3. Consulta su biblioteca personal.
4. Busca videojuegos utilizando una API externa.
5. Añade juegos a su colección.
6. Gestiona el progreso y la información de cada título.


##  Funcionalidades

### Usuarios
- Registro de usuarios.
- Inicio de sesión.
- Gestión de sesiones.
- Control de acceso.

### Biblioteca
- Añadir videojuegos.
- Consultar catálogo personal.
- Visualizar detalles.
- Actualizar estado del juego.

### Búsqueda
- Integración con API externa.
- Consulta de información actualizada.
- Búsqueda rápida de videojuegos.

##  Instalación

### Requisitos previos

- Python 3.10+
- Node.js 18+
- npm
- Git


### Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install django djangorestframework djangorestframework-simplejwt django-cors-headers django-filter

python manage.py migrate

python manage.py runserver
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

##  Variables de entorno

### Backend (.env)

```env
SECRET_KEY=your_secret_key
DEBUG=True
API_KEY=your_external_api_key
```

### Frontend (.env)

```env
VITE_API_URL=http://localhost:8000/api
```


##  Mejoras futuras

- Sistema de valoraciones y reseñas.
- Colecciones compartidas entre usuarios.
- Recomendaciones personalizadas.
- Escaneo automático de portadas.
- Estadísticas de progreso.
- Integración con plataformas gaming.

##  Documentación

La aplicación ha sido desarrollada como proyecto de fin de ciclo de **Desarrollo de Aplicaciones Web (DAW)**.

##  Autor

**Kevin Touriño Tabera**

Proyecto Final de Ciclo – DAW 2º
