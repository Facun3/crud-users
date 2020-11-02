 from django import forms
 from .models import Persona
 class PersonaForm(forms.ModelForm):
     class Meta:
         modelo = Persona
         field =[
             'nombre',
             'apellido',
             'correo',
             'dni',
             'domicilio',
             'nac',
             'alta_sistema',
         ]
