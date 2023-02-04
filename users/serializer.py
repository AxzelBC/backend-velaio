# Librerias Django
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

# Modelos
from users.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "username", "email", "password", "is_active", "documento"]

    def validate(self, attrs):
        email_exist = Usuario.objects.filter(email=attrs["email"]).exists()

        if email_exist:
            ValidationError("El usuario ya está registrado")

        return super().validate(attrs)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.password = validated_data.get("password", instance.password)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.documento = validated_data.get("documento", instance.documento)

        return super().update(instance, validated_data)
