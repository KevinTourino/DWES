from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    edad = models.IntegerField()
    activo = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ["username"]
        verbose_name = "Usuario"

    def __str__(self):
        return self.username


class Perfil(models.Model):
    usuario = models.OneToOneField(
            Usuario,
            on_delete=models.CASCADE,
            related_name="perfil"
    			)
    avatar = models.CharField(max_length=100)
    idioma = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Perfil de usuario"

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Género"

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.IntegerField()
    fecha_estreno = models.DateField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)
    generos = models.ManyToManyField(Genero, through='PeliculaGenero')  # AÑADIR ESTO

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Película"

    def __str__(self):
        return self.titulo



class PeliculaGenero(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    orden = models.IntegerField(default=1)  # Ejemplo: orden de importancia del género
    fecha_asignacion = models.DateField(auto_now_add=True)  # Cuándo se asignó

    class Meta:
        verbose_name = "Género de película"
        constraints = [
            models.UniqueConstraint(
                fields=['pelicula', 'genero'],
                name='unique_pelicula_genero'
            )
        ]

    def __str__(self):
        return f"{self.pelicula.titulo} - {self.genero.nombre}"


class Resena(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    comentario = models.CharField(max_length=255)
    fecha = models.DateField()

    class Meta:
        ordering = ["-fecha"]
        verbose_name = "Reseña"

    def __str__(self):
        return f"{self.usuario.username} - {self.pelicula.titulo}"


class Visualizacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    fecha_visualizacion = models.DateField()
    minutos_vistos = models.IntegerField()

    class Meta:
        verbose_name = "Visualización"

    def __str__(self):
        return f"{self.usuario.username} vio {self.pelicula.titulo} el {self.fecha_visualizacion}"