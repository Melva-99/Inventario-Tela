from django.contrib import admin
from .models import *

# Register your models here.
class EstanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class TelaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'diseno', 'calidad', 'color', 'numeroRollo')

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'estante', 'tela', 'diseno' , 'cantidadYarda', 'fecha')

class DetalleSalidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'nombre', 'diseno', 'calidad', 'color', 'numeroRollo', 'cantidadYarda', 'estante')

admin.site.register(Estante,EstanteAdmin) 

admin.site.register(Tela,TelaAdmin)

admin.site.register(Inventario,InventarioAdmin)

admin.site.register(DetalleSalida,DetalleSalidaAdmin)