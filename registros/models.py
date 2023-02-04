from django.db import models

# Create your models here.


class TipoPeticion(models.TextChoices):
    NEW = "new"
    TIME = "time"


class Registro(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    tipoPeticion = models.CharField(
        max_length=10, choices=TipoPeticion.choices, null=False
    )
    fecha = models.DateTimeField(auto_now_add=True, null=False)
    enlace = models.CharField(max_length=300, null=False)

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = "registro"
        verbose_name_plural = "registros"


class Noticias(Registro):
    autor = models.CharField(max_length=100, null=False)
    titular = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=1000, null=False)

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"


class Tiempo(Registro):
    hora = models.TimeField(null=False)

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = "tiempo"
        verbose_name_plural = "tiempos"
