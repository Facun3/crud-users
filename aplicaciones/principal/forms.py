from django import forms
from .models import Persona
from django.forms import ModelForm

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'