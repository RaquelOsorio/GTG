__author__ = 'viviana'

from django.forms import ModelForm
from django import forms
from gtg.models import inicio_sesion

class InicioForm(forms.Form):
    nombre = forms.CharField()
contrasena = forms.CharField(widget=forms.Textarea)
confirmar = forms.CharField(widget=forms.Textarea)

