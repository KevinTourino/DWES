from django.contrib.auth.models import User
from rest_framework import serializers


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