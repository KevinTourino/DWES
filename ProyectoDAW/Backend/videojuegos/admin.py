from django.contrib import admin

from .models import Videojuego, Plataforma, VideojuegoPlataforma, Biblioteca

admin.site.register(Videojuego)
admin.site.register(Plataforma)
admin.site.register(VideojuegoPlataforma)
admin.site.register(Biblioteca)
