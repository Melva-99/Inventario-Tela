from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.index, name='index'),
    #ESTANTE1
    path('inventario/', views.inventario, name='inventario'),
    path('entrada/', views.entrada, name='entrada'),
    path('salida/', views.salida, name='salida'),
    path('salida/<int:id>/<int:id_estante>/salida', views.salidaTelas , name="salidaTelas"),
    path('detalleSalida/', views.detalleSalida, name='detalleSalida'),
    path('salidaPdf/',views.salidaPdf.as_view(),name='salidaPdf',
    
    ),
]