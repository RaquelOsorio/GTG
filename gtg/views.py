
from gtg.forms import InicioForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from gtg.models import inicio_sesion
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