from django import forms 
from .models import Practica

class PracticaForm(forms.ModelForm):
    class Meta:
        model = Practica
        fields = ['nombre', 'email', 'mensaje']