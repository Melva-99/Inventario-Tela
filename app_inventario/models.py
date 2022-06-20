from django.db import models
from django.db.models.fields import FloatField
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey


class Estante(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'


class Tipo_Tela(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'

class Tela(models.Model):
    nombre = models.CharField(max_length=30)
    calidad = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    numeroRollo = models.IntegerField()
    tipoTela = models.ForeignKey(Tipo_Tela,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}'

class Inventario(models.Model):
    estante = models.ForeignKey(Estante, on_delete=models.CASCADE)
    tela = models.ForeignKey(Tela, related_name="nombreTela", on_delete=models.CASCADE)
    cantidadYarda = models.FloatField()

    def __str__(self):
        return f'{self.estante} {self.tela}'

class Transferencia(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cantidadYarda = models.IntegerField()
    estanteOrigen = models.ForeignKey(Estante,related_name="estanteOrigen" ,on_delete=models.CASCADE)
    estanteDestino = models.ForeignKey(Estante,related_name="estanteDestino" ,on_delete=models.CASCADE)
    telaProduc = models.ForeignKey(Tela, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.telaProduc} - Origen: {self.estanteOrigen}  - Destino: {self.estanteDestino}'

class DetalleSalida(models.Model):

    fecha = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=30)
    calidad = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    numeroRollo = models.IntegerField()
    cantidadYarda = models.FloatField()
    estante = models.ForeignKey(Estante, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fecha} {self.nombre}'