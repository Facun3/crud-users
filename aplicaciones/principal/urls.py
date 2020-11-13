from django.urls import path 
from . import views
from .models import Persona
from aplicaciones.principal.views import crearusuario,inicio
urlpatterns = [
    path('', inicio, name='inicio'),
    path('new/', crearusuario, name='crear_usuario'),
]