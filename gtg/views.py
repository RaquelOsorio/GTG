from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.shortcuts import render_to_response
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

def ingresar(request):
    """controla si el usuario se encuentra registrado, permite iniciar sesion
    :param request:
    :return retorna a la siguiente intefaz
    C{import} Importa variables.
    C{variables} todas las variables.
     """
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
    """permite acceder a la siguiente interfaz de modulos del proyecto"""
    usuario = request.user
    return render_to_response('base.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/ingresar')
def administrar(request):
    """permite acceder a la siguiente interfaz de modulo de administracion"""
    return render_to_response('prueba.html',context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def desarrollo(request):
    """permite acceder a la siguiente interfaz de modulo de administracion"""
    return render_to_response('desarrollo.html',context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def administrar(request):
   # html = render_to_response('prueba.html')
    return render_to_response('prueba.html',context_instance=RequestContext(request))

def configuracion(request):
    """permite acceder a la siguiente interfaz de modulo de administracion"""
    return render_to_response('configuracion.html',context_instance=RequestContext(request))

def tipoAtributo(request):
    """permite acceder a la interfaz de opciones de administracion para los tipos de atributos"""
    return render_to_response('gestionAtributo.html',context_instance=RequestContext(request))

def usuario(request):
    """permite acceder a la interfaz de opciones de administracion para usuarios"""
    return render_to_response('gestionUsuario.html',context_instance=RequestContext(request))

def proyecto(request):
    """permite acceder a la interfaz de opciones de administracion para proyectos"""
    return render_to_response('gestionProyecto.html',context_instance=RequestContext(request))

def fase(request):
    """permite acceder a la interfaz de opciones de administracion para fases"""
    return render_to_response('gestionFase.html',context_instance=RequestContext(request))

def rolPermiso(request):
    """permite acceder a la interfaz de opciones de roles y permisos"""
    return render_to_response('gestionRolesPermisos.html',context_instance=RequestContext(request))

def tipoItem(request):
    """permite acceder a la interfaz de opciones de tipo de Item"""
    return render_to_response('gestionTipoItem.html',context_instance=RequestContext(request))

def item(request):
    """permite acceder a la interfaz de opciones de administracion para items"""
    return render_to_response('gestionItem.html',context_instance=RequestContext(request))

def lb(request):
    """permite acceder a la interfaz de opciones de linea base"""
    return render_to_response('gestionLB.html',context_instance=RequestContext(request))

def cambio(request):
    """permite acceder a la interfaz de opciones de administracion para Solicitudes de cambio"""
    return render_to_response('gestionCambio.html',context_instance=RequestContext(request))

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

def updatecombo(request, option):
    dajax = Dajax()
    options = [['Madrid', 'Barcelona', 'Vitoria', 'Burgos'],
               ['Paris', 'Evreux', 'Le Havre', 'Reims'],
               ['London', 'Birmingham', 'Bristol', 'Cardiff']]
    out = []
    for option in options[int(option)]:
        out.append("<option value='#'>%s</option>" % option)

    dajax.assign('#combo2', 'innerHTML', ''.join(out))
    return dajax.json()