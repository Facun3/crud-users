from .models import Persona
from .forms import PersonaForm
from django.shortcuts import render, redirect
from django.http import *
from django.utils import timezone
def inicio(request):
    personas =  Persona.objects.all()
    contexto = {
        'personas':personas
    }
    return render(request,'index.html',contexto)

def crearusuario(request):
    form = PersonaForm()
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            guardar = form.save(commit=True)
            redirect(inicio)
        else:
            form = PersonaForm()
    return render(request,'crear_usuario.html',{'form':form})


