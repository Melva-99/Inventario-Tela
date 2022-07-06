from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.index, name='index'),
    #ESTANTE1
    path('inventarioE1/', views.inventarioE1, name='inventarioE1'),
    path('entradaE1/', views.entradaE1, name='entradaE1'),
    path('salidaE1/', views.salidaE1, name='salidaE1'),
    path('salidaE1/<int:id>/<int:id_estante>/salida', views.salidaTelas , name="salidaTelas"),
    #ESTANTE 2
    path('inventarioE2/', views.inventarioE2, name='inventarioE2'),
    path('entradaE2/', views.entradaE2, name='entradaE2'),
    path('salidaE2/', views.salidaE2, name='salidaE2'),
    path('salidaE2/<int:id>/<int:id_estante>/salida', views.salidaTelas2 , name="salidaTelas2"),
    #ESTANTE 3
    path('inventarioE3/', views.inventarioE3, name='inventarioE3'),
    path('entradaE3/', views.entradaE3, name='entradaE3'),
    path('salidaE3/', views.salidaE3, name='salidaE3'),
    path('salidaE3/<int:id>/<int:id_estante>/salida', views.salidaTelas3 , name="salidaTelas3"),
    #ESTANTE 4
    path('inventarioE4/', views.inventarioE4, name='inventarioE4'),
    path('entradaE4/', views.entradaE4, name='entradaE4'),
    path('salidaE4/', views.salidaE4, name='salidaE4'),
    path('salidaE4/<int:id>/<int:id_estante>/salida', views.salidaTelas4 , name="salidaTelas4"),
    #ESTANTE 5
    path('inventarioE5/', views.inventarioE5, name='inventarioE5'),
    path('entradaE5/', views.entradaE5, name='entradaE5'),
    path('salidaE5/', views.salidaE5, name='salidaE5'),
    path('salidaE5/<int:id>/<int:id_estante>/salida', views.salidaTelas5 , name="salidaTelas5"),
    #ESTANTE 6
    path('inventarioE6/', views.inventarioE6, name='inventarioE6'),
    path('entradaE6/', views.entradaE6, name='entradaE6'),
    path('salidaE6/', views.salidaE6, name='salidaE6'),
    path('salidaE6/<int:id>/<int:id_estante>/salida', views.salidaTelas6 , name="salidaTelas6"),
    
]