
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from gtg.models import Rol
from gtg.forms import rolForm
from gtg.models import Proyecto
from gtg.forms import proyectoForm
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
import os
from os.path import join,realpath
from django.conf import settings

from django.shortcuts import render_to_response


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


def registrarRol(request):
        """Permite registrar un nuevo rol en el sistema"""
	if request.method == "POST":
		formulario = rolForm(request.POST, request.FILES)

		if formulario.is_valid():
			#forma para poder ingresar a los datos del formulario, tal vez para hacer nuestras propias validaciones
			print "==============================================="
			print formulario.cleaned_data['nombre']
			print "==============================================="
			formulario.save()
			return HttpResponseRedirect('/rolPermiso')

	else:
		formulario=rolForm()

	return render(request, 'rol_form.html', {'formulario': formulario,})

def lista_roles(request):
	roles=Rol.objects.all()
	# return render(request, 'index.html', {'usuarios': usuarios,})
	return render_to_response('roles.html', {'roles': roles}, context_instance=RequestContext(request))

def eliminar_rol(request):
    rol=Rol.objects.get(pk="4")
    rol.delete()
    return HttpResponseRedirect('/rolPermiso')


def registrarProyecto(request):
        """Permite registrar un nuevo proyecto en el sistema"""
	if request.method == "POST":
		formulario = proyectoForm(request.POST, request.FILES)

		if formulario.is_valid():
			#forma para poder ingresar a los datos del formulario, tal vez para hacer nuestras propias validaciones
			print "==============================================="
			print formulario.cleaned_data['nombre']
			print "==============================================="
			formulario.save()
			return HttpResponseRedirect('/proyecto')

	else:
		formulario=proyectoForm()

	return render(request, 'proyecto_form.html', {'formulario': formulario,})


