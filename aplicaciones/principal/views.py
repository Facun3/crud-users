from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import PersonaForm

def inicio(request):
    personas =  Persona.objects.all()
    contexto = {
        'personas':personas
    }
    return render(request,'index.html',contexto)

def crearusuario(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)


