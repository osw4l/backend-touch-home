from django.contrib.auth.models import User
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from . import constants


# Create your models here.


class Profesion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    cover = models.URLField(default=constants.URL_COVER)

    class Meta:
        verbose_name = 'Profesion'
        verbose_name_plural = 'Profesiones'

    def __str__(self):
        return self.nombre

    def profesionales(self):
        return Profesional.objects.filter(profesion=self)


class Profesional(models.Model):
    nombre_completo = models.CharField(max_length=60)
    telefono = models.CharField(max_length=14)
    correo = models.EmailField()
    profesion = models.ForeignKey(Profesion)

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

