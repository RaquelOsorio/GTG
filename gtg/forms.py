__author__ = 'viviana'


from django import forms
<<<<<<< HEAD
from gtg.models import Rol
=======
<<<<<<< HEAD
from gtg.models import Roles
>>>>>>> fe7246aeac811a8fed1421c108919f8234490cf0
from gtg.models import Usuario
from gtg.models import Usuario_rol
from django.contrib.auth.forms import UserCreationForm
from gtg.models import ModificarRol
from gtg.models import Fase
<<<<<<< HEAD
from gtg.models import RolUsuario
=======
from gtg.models import RolesUsuario
>>>>>>> fe7246aeac811a8fed1421c108919f8234490cf0
from gtg.models import TipoAtributo
from gtg.models import Proyectos
from gtg.models import Fases1
from gtg.models import TipoItem
<<<<<<< HEAD


class rolForm(forms.ModelForm):
    class Meta:
        model=Rol
=======
from gtg.models import Item

class RolForm(forms.ModelForm):
    class Meta:
        model=Roles
>>>>>>> fe7246aeac811a8fed1421c108919f8234490cf0

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

class FaseForm(forms.ModelForm):
    class Meta:
        model=Fase

<<<<<<< HEAD
class rolusuarioForm(forms.ModelForm):
    class Meta:
        model=RolUsuario

class TipoAtributoForm(forms.ModelForm):
    class Meta:
        model= TipoAtributo

class TipoItemForm(forms.ModelForm):
    class Meta:
        model= TipoItem
=======
class RolusuarioForm(forms.ModelForm):
    class Meta:
        model=RolesUsuario

class TipoAtributoForm(forms.ModelForm):
    class Meta:
        model= TipoAtributo
=======
<<<<<<< HEAD
from gtg.models import Rol
from gtg.models import Proyecto



class rolForm(forms.ModelForm):
    class Meta:
        model=Rol


class proyectoForm(forms.ModelForm):
    class Meta:
        model=Proyecto
>>>>>>> 64570d5fc03175bcdd7814fba88c89225e9a231d

class TipoItemForm(forms.ModelForm):
    class Meta:
        model= TipoItem

<<<<<<< HEAD
class ItemForm(forms.ModelForm):
    class Meta:
        model= Item
=======
=======
>>>>>>> 422ad2cad28d48cc948a7890ed3910fb77c281e1
>>>>>>> 64570d5fc03175bcdd7814fba88c89225e9a231d
>>>>>>> fe7246aeac811a8fed1421c108919f8234490cf0
