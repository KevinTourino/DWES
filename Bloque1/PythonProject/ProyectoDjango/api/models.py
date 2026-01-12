from django.db import models

class Curso(models.Model):
    NIVEL_CHOICES = [
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]

    titulo = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    nivel = models.CharField(max_length=15, choices=NIVEL_CHOICES)

    def __str__(self):
        return self.titulo