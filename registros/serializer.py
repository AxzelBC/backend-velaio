# Librerias Django
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
import validators

# Modelos
from registros.models import Registro, Noticias, Tiempo


class RegistrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = "__all__"


class NoticiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticias
        fields = "__all__"

    def validate(self, attrs):
        enlace_valid = validators.url(attrs["enlace"])

        if not enlace_valid:
            ValidationError("Enlace invalido")

        return super().validate(attrs)

    def update(self, instance, validated_data):
        instance.tipoPeticion = validated_data.get(
            "tipoPeticion", instance.tipoPeticion
        )
        instance.enlace = validated_data.get("enlace", instance.enlace)
        instance.autor = validated_data.get("autor", instance.autor)
        instance.titular = validated_data.get("titular", instance.titular)
        instance.descripcion = validated_data.get("descripcion", instance.descripcion)

        return super().update(instance, validated_data)


class TiempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiempo
        fields = "__all__"

    def validate(self, attrs):
        enlace_valid = validators.url(attrs["enlace"])

        if not enlace_valid:
            ValidationError("Enlace invalido")

        return super().validate(attrs)

    def update(self, instance, validated_data):
        instance.tipoPeticion = validated_data.get(
            "tipoPeticion", instance.tipoPeticion
        )
        instance.enlace = validated_data.get("enlace", instance.enlace)
        instance.ciudad = validated_data.get("ciudad", instance.ciudad)
        instance.humedad = validated_data.get("humedad", instance.humedad)
        instance.temp = validated_data.get("temp", instance.temp)

        return super().update(instance, validated_data)
