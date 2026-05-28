from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (
    Biblioteca,
    Plataforma,
    Videojuego,
    VideojuegoPlataforma
)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("El email ya existe")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("El usuario ya existe")
        return value

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Mínimo 6 caracteres")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    








class PlataformaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plataforma
        fields = ["id", "nombre", "codigo"]


class VideojuegoPlataformaSerializer(serializers.ModelSerializer):

    plataforma = PlataformaSerializer(read_only=True)

    class Meta:
        model = VideojuegoPlataforma
        fields = [
            "id",
            "plataforma",
            "fecha_lanzamiento",
            "version",
            "exclusivo"
        ]


class VideojuegoSerializer(serializers.ModelSerializer):

    plataformas = VideojuegoPlataformaSerializer(
        source="videojuegoplataforma_set",
        many=True,
        read_only=True
    )

    class Meta:
        model = Videojuego
        fields = [
            "id",
            "titulo",
            "descripcion",
            "precio",
            "fecha_lanzamiento",
            "plataformas"
        ]


class BibliotecaSerializer(serializers.ModelSerializer):

    videojuego = VideojuegoSerializer(read_only=True)

    videojuego_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Biblioteca
        fields = [
            "id",
            "videojuego",
            "videojuego_id",
            "fecha_compra"
        ]
        read_only_fields = ["fecha_compra"]

    def create(self, validated_data):
        usuario = self.context["request"].user
        videojuego_id = validated_data.pop("videojuego_id")

        videojuego, _ = Videojuego.objects.get_or_create(
            id=videojuego_id
        )

        biblioteca, created = Biblioteca.objects.get_or_create(
            usuario=usuario,
            videojuego=videojuego
        )

        return biblioteca