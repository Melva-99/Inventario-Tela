from django.contrib import admin
from .models import *

# Register your models here.
class EstanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class Tipo_TelaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class TelaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'calidad', 'color', 'numeroRollo', 'tipoTela')

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'estante', 'tela', 'cantidadYarda')

class DetalleSalidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'nombre', 'calidad', 'color', 'numeroRollo', 'cantidadYarda', 'estante')

admin.site.register(Estante,EstanteAdmin) 

admin.site.register(Tipo_Tela,Tipo_TelaAdmin)

admin.site.register(Tela,TelaAdmin)

admin.site.register(Inventario,InventarioAdmin)

admin.site.register(DetalleSalida,DetalleSalidaAdmin)