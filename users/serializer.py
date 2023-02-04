# Librerias Django
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# Modelos


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_active"]

    def validate(self, attrs):
        email_exist = self.Meta.model.objects.filter(email=attrs["email"]).exists()

        if email_exist:
            ValidationError("El usuario ya está registrado")
            
        attrs['password'] = make_password(attrs['password'])

        return super().validate(attrs)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.password = validated_data.get("password", instance.password)
        instance.is_active = validated_data.get("is_active", instance.is_active)

        return super().update(instance, validated_data)
