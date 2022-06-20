"""Inventario_Tela URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_inventario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('inventarioE1/', views.inventarioE1, name='inventarioE1'),
    path('entradaE1/', views.entradaE1, name='entradaE1'),
    path('salidaE1/', views.salidaE1, name='salidaE1'),
    path('verSalidaE1/', views.verSalidaE1, name='verSalidaE1'),
    path('salidaE1/<int:id>/<int:id_estante>/salida', views.salidaTelas , name="salidaTelas"),
    
]
