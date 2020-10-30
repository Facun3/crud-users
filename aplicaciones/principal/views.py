from django.shortcuts import render
from .models import Persona

def inicio(request):
    personas =  Persona.objects.
    return render(request,'index.html')
