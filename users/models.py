from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(User):
    documento = models.CharField(null=False, unique=True, max_length=15)

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __int__(self):
        return self.id
