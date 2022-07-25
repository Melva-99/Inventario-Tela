from django.db import models
from django.db.models.fields import FloatField
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey


class Estante(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'


class Tela(models.Model):
    nombre = models.CharField(max_length=30)
    diseno = models.IntegerField()
    calidad = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    numeroRollo = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}'

class Inventario(models.Model):
    estante = models.ForeignKey(Estante, on_delete=models.CASCADE)
    tela = models.ForeignKey(Tela, related_name="nombreTela", on_delete=models.CASCADE)
    diseno = models.IntegerField()
    cantidadYarda = models.FloatField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.estante} {self.tela}'

class DetalleSalida(models.Model):

    fecha = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=30)
    diseno = models.IntegerField()
    calidad = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    numeroRollo = models.IntegerField()
    cantidadYarda = models.FloatField()
    estante = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.fecha} {self.nombre}'