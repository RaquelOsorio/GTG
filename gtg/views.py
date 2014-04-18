from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

from django.shortcuts import render_to_response


def ingresar(request):
    """@ param """
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render_to_response('base.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

def administrar(request):
   # html = render_to_response('prueba.html')
    return render_to_response('prueba.html',context_instance=RequestContext(request))

def configuracion(request):
    """permite acceder a la siguiente interfaz de modulo de administracion"""
    return render_to_response('configuracion.html',context_instance=RequestContext(request))

def tipoAtributo(request):
    """permite acceder a la siguiente interfaz de modulo de administracion"""
    return render_to_response('gestionAtributo.html',context_instance=RequestContext(request))

def proyecto(request):
    """permite acceder a la siguiente interfaz de modulo de administracion"""
    return render_to_response('gestionProyecto.html',context_instance=RequestContext(request))

def rolesPermisos(request):
    """permite acceder a la siguiente interfaz de modulo de administracion"""
    return render_to_response('gestionRolesPermisos.html',context_instance=RequestContext(request))

def tipoItem(request):
    """permite acceder a la siguiente interfaz de modulo de administracion"""
    return render_to_response('gestionTipoItem.html',context_instance=RequestContext(request))

def solicitudCambio(request):
    """permite acceder a la siguiente interfaz de modulo de administracion"""
    return render_to_response('gestionSolicitud.html',context_instance=RequestContext(request))

def altaUsuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/administrar')
    else:
        form= UserCreationForm()
    return render_to_response('altaUsuario.html', {'form':form}, context_instance=RequestContext(request))

