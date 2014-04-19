__author__ = 'viviana'


from django import forms
from gtg.models import Rol
from gtg.models import Proyecto



class rolForm(forms.ModelForm):
    class Meta:
        model=Rol


class proyectoForm(forms.ModelForm):
    class Meta:
        model=Proyecto


