from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    nombre = models.CharField(max_length=200)
    anio_lanzamiento = models.DateField()
    descripcion = models.TextField()
    generos = models.ManyToManyField(Genero)
    coverUrl = models.TextField()

    def __str__(self):
        return self.nombre


class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class BibliotecaUsuario(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("jugando", "Jugando"),
        ("completado", "Completado"),
        ("abandonado", "Abandonado"),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="pendiente"
    )

    fecha_agregado = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="biblioteca"
    )

    videojuego = models.ForeignKey(
        Videojuego,
        on_delete=models.CASCADE,
        related_name="usuarios"
    )

    plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.CASCADE,
        related_name="biblioteca"
    )

    class Meta:
        unique_together = ("usuario", "videojuego", "plataforma")

    def __str__(self):
        return f"{self.usuario} - {self.videojuego} ({self.plataforma})"