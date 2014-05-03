__author__ = 'viviana'


from django import forms
from gtg.models import Rol
from gtg.models import Usuario
from gtg.models import Usuario_rol
from django.contrib.auth.forms import UserCreationForm
from gtg.models import ModificarRol
from gtg.models import RolUsuario
from gtg.models import TipoAtributo
from gtg.models import Proyectos
from gtg.models import Fases1
from gtg.models import TipoItem
from gtg.models import Item


class rolForm(forms.ModelForm):
    class Meta:
        model=Rol

class ProyectoForm(forms.ModelForm):
    class Meta:
        model= Proyectos

class Fases1Form(forms.ModelForm):
    class Meta:
        model=Fases1

class usuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(usuarioForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
       # if commit:
        #    user.save()
        #return user
        #def save(self, commit=True):
#    user = super(usuarioForm).save(commit=False)
        #   user.email = self.cleaned_data["email"]
        #if commit:
         #   user.save()
        #return user

class ModificarRolForm(forms.ModelForm):
    class Meta:
        model=ModificarRol



class TipoAtributoForm(forms.ModelForm):
    class Meta:
        model= TipoAtributo

class TipoItemForm(forms.ModelForm):
    class Meta:
        model= TipoItem


class ItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields=("nroItem","nombre","estado","version","prioridad","descripcion","tipoItem","fase")

class relacionarForm(forms.ModelForm):
    class Meta:
        model= Item
        fields=("antecesorHorizontal","antecesorVertical")


class rolusuarioForm(forms.ModelForm):
    class Meta:
        model=RolUsuario

