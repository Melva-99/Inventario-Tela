from django.urls import include, path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('inventario/', include('app_inventario.urls')),
    path('RegistroUsuario/',views.RegistroUsuario.as_view(),name='RegistroUsuario'),
]