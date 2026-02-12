from rest_framework import serializers
from .models import Pelicula, Usuario, Perfil, Genero, PeliculaGenero, Resena, Visualizacion


# ===== SERIALIZERS BÁSICOS =====
class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nombre']


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['id', 'usuario', 'avatar', 'idioma']


# ===== RELACIÓN 1:1 (Usuario <-> Perfil) =====
class UsuarioSerializer(serializers.ModelSerializer):
    perfil_id = serializers.PrimaryKeyRelatedField(
        queryset=Perfil.objects.all(),
        source='perfil',
        write_only=True,
        required=False
    )
    perfil = PerfilSerializer(read_only=True)
    
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'edad', 'activo', 
                  'created_at', 'updated_at', 'perfil', 'perfil_id']
        read_only_fields = ['created_at', 'updated_at']


# ===== RELACIÓN 1:N (Pelicula -> Resenas) =====
class ResenaSerializer(serializers.ModelSerializer):
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(),
        source='usuario',
        write_only=True
    )
    usuario = serializers.StringRelatedField(read_only=True)
    
    pelicula_id = serializers.PrimaryKeyRelatedField(
        queryset=Pelicula.objects.all(),
        source='pelicula',
        write_only=True
    )
    pelicula = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Resena
        fields = ['id', 'usuario', 'usuario_id', 'pelicula', 'pelicula_id',
                  'puntuacion', 'comentario', 'fecha']


# ===== RELACIÓN N:M CON MODELO INTERMEDIO (Pelicula <-> Genero) =====
class PeliculaGeneroSerializer(serializers.ModelSerializer):
    genero_nombre = serializers.CharField(source='genero.nombre', read_only=True)
    pelicula_titulo = serializers.CharField(source='pelicula.titulo', read_only=True)
    
    class Meta:
        model = PeliculaGenero
        fields = ['id', 'pelicula', 'pelicula_titulo', 'genero', 
                  'genero_nombre', 'orden', 'fecha_asignacion']


# ===== SERIALIZER DE PELICULA CON RELACIONES =====
class PeliculaSerializer(serializers.ModelSerializer):
    resenas = ResenaSerializer(many=True, read_only=True, source='resena_set')
    generos_detalle = PeliculaGeneroSerializer(
        many=True, 
        read_only=True, 
        source='peliculagenero_set'
    )
    
    class Meta:
        model = Pelicula
        fields = ['id', 'titulo', 'duracion', 'fecha_estreno', 'precio', 
                  'disponible', 'resenas', 'generos_detalle']


# ===== RELACIÓN N:M SIMPLE =====
class VisualizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visualizacion
        fields = ['id', 'usuario', 'pelicula', 'fecha_visualizacion', 'minutos_vistos']


# ===== SERIALIZERS PARA ACCIONES DE NEGOCIO =====

# Serializer para marcar película como vista
class MarcarVistaSerializer(serializers.Serializer):
    minutos_vistos = serializers.IntegerField(min_value=1)
    fecha_visualizacion = serializers.DateField(required=False)
    
    def validate_minutos_vistos(self, value):
        pelicula = self.context.get('pelicula')
        if pelicula and value > pelicula.duracion:
            raise serializers.ValidationError(
                f"Los minutos vistos ({value}) no pueden superar la duracion de la pelicula ({pelicula.duracion})"
            )
        return value


# Serializer para cambiar precio
class CambioPrecioSerializer(serializers.Serializer):
    nuevo_precio = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=0)
    motivo = serializers.CharField(max_length=200, required=False)


# Serializer para añadir reseña desde la película
class AgregarResenaSerializer(serializers.Serializer):
    puntuacion = serializers.IntegerField(min_value=1, max_value=5)
    comentario = serializers.CharField(max_length=255)
    
    def validate_puntuacion(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("La puntuacion debe estar entre 1 y 5")
        return value