from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Videojuego, Plataforma, BibliotecaUsuario, Genero


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
    








class BibliotecaSerializer(serializers.ModelSerializer):
    videojuego = serializers.DictField(write_only=True)
    plataformas = serializers.DictField(write_only=True)

    class Meta:
        model = BibliotecaUsuario
        fields = ["videojuego", "plataformas"]

    def create(self, validated_data):
        request = self.context["request"]
        usuario = request.user

        videojuego_data = validated_data.pop("videojuego")
        plataformas_data = validated_data.pop("plataformas")

        generos = videojuego_data.pop("generos", [])

        videojuego, _ = Videojuego.objects.get_or_create(
            nombre=videojuego_data["nombre"],
            defaults=videojuego_data
        )

        # 🎮 géneros
        for nombre_genero in generos:
            genero, _ = Genero.objects.get_or_create(nombre=nombre_genero)
            videojuego.generos.add(genero)

        # 📱 plataformas
        for nombre_plataforma, estado in plataformas_data.items():
            plataforma, _ = Plataforma.objects.get_or_create(nombre=nombre_plataforma)

            BibliotecaUsuario.objects.create(
                usuario=usuario,
                videojuego=videojuego,
                plataforma=plataforma,
                estado=estado
            )

        return {
            "message": "Biblioteca creada correctamente",
        }