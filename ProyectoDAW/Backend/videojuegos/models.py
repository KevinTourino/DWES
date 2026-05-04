from django.db import models
from django.contrib.auth.models import User

class Plataforma(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    codigo = models.CharField(max_length=10, unique=True, help_text="Ej: PS5, XBOX, PC")

    def __str__(self):
        return self.nombre


class Videojuego(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    precio = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    fecha_lanzamiento = models.DateField(null=True, blank=True)

    # Relación N:M con tabla intermedia
    plataformas = models.ManyToManyField(Plataforma, through='VideojuegoPlataforma')

    def __str__(self):
        return self.titulo


class VideojuegoPlataforma(models.Model):
    """Tabla intermedia (through)"""

    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)

    fecha_lanzamiento = models.DateField()
    version = models.CharField(max_length=50, blank=True)
    exclusivo = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['videojuego', 'plataforma'],
                name='unique_videojuego_plataforma'
            )
        ]

    def __str__(self):
        return f"{self.videojuego} en {self.plataforma}"

class Biblioteca(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)

    fecha_compra = models.DateTimeField(auto_now_add=True)