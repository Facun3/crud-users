from django.shortcuts import render
from .models import Persona

def inicio(request):
    personas =  Persona.objects.all()
    contexto = {
        'personas':personas
    }
    return render(request,'index.html',contexto)
