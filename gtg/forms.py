__author__ = 'viviana'


from django import forms
from gtg.models import Rol
from gtg.models import Usuario
from gtg.models import Usuario_rol
from django.contrib.auth.forms import UserCreationForm

from gtg.models import RolUsuario
from gtg.models import TipoAtributo
from gtg.models import Proyectos
from gtg.models import Fases1
from gtg.models import TipoItem
from gtg.models import Item
from gtg.models import ItemRelacion
from gtg.models import lineaBase
from django.forms import Select

class rolForm(forms.ModelForm):
    class Meta:
        model=Rol

class ProyectoForm(forms.ModelForm):
    class Meta:
        model= Proyectos
        fields = ("fechaInicio","fechaFin","nombre","complejidad","lider")

class Fases1Form(forms.ModelForm):
    class Meta:
        model=Fases1
        fields =(
            "fechaInicio",
            "fechaFin",
            "nombre",
            "descripcion",
            #"proyecto",

        )

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




class TipoAtributoForm(forms.ModelForm):
    class Meta:
        model= TipoAtributo

class TipoItemForm(forms.ModelForm):
    class Meta:
        model= TipoItem


class ItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields=("id","nombre","prioridad","descripcion","tipoItem","fase")
    def clean(self):

    # get bitcoin address from form
        name =  self.cleaned_data.get('nombre')
        i=0
        ite=Item.objects.all()
        for it in ite:
            print self.cleaned_data.get('nombre')
            if (name == it.nombre):
                raise forms.ValidationError('Ya existe un item con ese nombre.')
            i=1
        return self.cleaned_data


class ItemForm1(forms.ModelForm):
    class Meta:
        model= Item
        fields=("estado","nombre","version","prioridad","descripcion","tipoItem","fase")



class ItemReversionar(forms.ModelForm):
    class Meta:
        model= Item
        fields=()




class relacionarForm(forms.ModelForm):
    class Meta:
        model= Item
        fields=("antecesorHorizontal","antecesorVertical","sucesorHorizontal","sucesorVertical")

class EliminarItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields=("estado",)


class rolusuarioForm(forms.ModelForm):
    class Meta:
        model=RolUsuario

class ItemRelacionForm(forms.ModelForm):
    """

    Formulario que permite la carga de relaciones items.

    """
    class Meta:
        model = ItemRelacion
        fields = ['origen', 'destino']
        widgets ={'origen': Select(attrs={'size': 10}),\
                  'destino': Select(attrs={'size': 10})}

class lbForm(forms.ModelForm):
    class Meta:
        model= lineaBase
        fields=()