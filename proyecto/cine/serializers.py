from rest_framework import serializers
from .models import Pelicula, Usuario


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = ['id', 'titulo', 'duracion', 'fecha_estreno', 'precio', 'disponible']


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'edad', 'activo', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']