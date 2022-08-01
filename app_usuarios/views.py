from django.contrib.auth.models import User
from django.views.generic import CreateView

from app_usuarios.forms import RegistroForm

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuarios/registrarUsuario.html"
    form_class = RegistroForm
    success_url = '/'

    
