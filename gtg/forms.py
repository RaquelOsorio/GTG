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
#from gtg.models import ItemRelacion
from gtg.models import lineaBase
from django.forms import Select
from gtg.models import Voto
from gtg.models import SolicitudCambio
from gtg.models import Comite

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
        fields=("id","nombre","prioridad","descripcion","tipoItem")
    def clean(self):

    # get bitcoin address from form
        name =  self.cleaned_data.get('nombre')
        i=0
        ite=Item.objects.all()
        for it in ite:
            print( self.cleaned_data.get('nombre'))
            if (name == it.nombre):
                raise forms.ValidationError('Ya existe un item con ese nombre.')
            i=1
        return self.cleaned_data


class ItemForm1(forms.ModelForm):
    class Meta:
        model= Item
        fields=("estado","nombre","prioridad")



class ItemReversionar(forms.ModelForm):
    class Meta:
        model= Item
        fields=("descripcion","prioridad")




class relacionarForm(forms.ModelForm):
    #antecesorHorizontal = forms.ModelChoiceField(queryset=Item.objects.all())
    #antecesorHorizontal = forms.ModelChoiceField(queryset=Item.objects.none())
    #antecesorVertical = forms.ModelChoiceField(queryset=Item.objects.none())
    class Meta:
        model= Item
        fields=()



    def clean(self):

        antecesorH =  self.cleaned_data.get('antecesorHorizontal')
        antecesorV =self.cleaned_data.get('antecesorVertical')
        print (self.cleaned_data.get('antecesorH'))
        print (self.cleaned_data.get('antecesorV'))
        if (antecesorH !=None  and antecesorV != None):
            raise forms.ValidationError('Un item solo puede tener un antecesor.')
        else:
            return self.cleaned_data

        ite=Item.objects.filter(self)
        ite2=Item.objects.filter(self)

        while(ite.antecesorHorizontal != None or ite.antecesorVertical != None):
            print( self.cleaned_data.get('nombre'))
            if (ite == ite2):
                while(ite.sucesorVertical != None):
                    ite=ite.sucesorVertical
                    print (self.cleaned_data.get('nombre'))
                    if (ite == antecesorV):
                        raise forms.ValidationError('Se forma un ciclo.')
                    else:
                        return self.cleaned_data

        return self.cleaned_data






class EliminarItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields=( )


class rolusuarioForm(forms.ModelForm):
    class Meta:
        model=RolUsuario


class lbForm(forms.ModelForm):
    class Meta:
        model= lineaBase
        fields=()

class ItemLbForm(forms.ModelForm):
    class Meta:
        model= Item
        fields=( )

class importarFaseForm(forms.ModelForm):
    class Meta:
        model=Fases1
        fields=('proyectos','nombre',)

class finalizarFaseForm(forms.ModelForm):
    class Meta:
        model=Fases1
        fields=()

class EliminarRelacionItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields=( )

class SolicitudCambioForm(forms.ModelForm):
    class Meta:
        model= SolicitudCambio
        fields=('nombre', 'descripcion',)


class VotoForm(forms.ModelForm):
    class Meta:
        model= Voto
        fields=('voto',)


class ComiteForm(forms.ModelForm):
    class Meta:
        model= Comite
        fields=()