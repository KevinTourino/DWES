from django.contrib import admin

from .models import Videojuego, Plataforma, BibliotecaUsuario, Genero


@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "anio_lanzamiento")
    search_fields = ("nombre",)
    list_filter = ("anio_lanzamiento",)


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(BibliotecaUsuario)
class BibliotecaUsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "videojuego", "plataforma", "estado", "fecha_agregado")
    list_filter = ("estado", "plataforma")
    search_fields = ("usuario__username", "videojuego__nombre")
    autocomplete_fields = ("usuario", "videojuego", "plataforma")


