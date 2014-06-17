
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.template import RequestContext
from django.contrib.auth.forms import User, UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import pydot
from django.db.models import Q
from datetime import datetime
from __builtin__ import file
from gtg.models import Usuario
from gtg.models import Rol
from gtg.models import Usuario
from gtg.forms import usuarioForm
from gtg.forms import rolForm
from gtg.forms import importarFaseForm
from gtg.forms import finalizarFaseForm
from gtg.forms import ItemFormVal
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
import os
from os.path import join,realpath
from django.conf import settings
from gtg.forms import rolusuarioForm
from gtg.models import RolUsuario
from django.shortcuts import render_to_response
from gtg.forms import ItemForm1
from gtg.models import TipoAtributo
from gtg.forms import relacionarForm
from gtg.forms import TipoAtributoForm
from gtg.models import Proyectos
from gtg.forms import ProyectoForm
from gtg.models import Fases1
from gtg.forms import Fases1Form
from gtg.models import TipoItem
from gtg.forms import TipoItemForm
from gtg.models import Item
from gtg.forms import ItemForm
from gtg.forms import ItemReversionar
from django.contrib import messages
from gtg.forms import ItemForm1
#from gtg.models import ItemRelacion
#from gtg.forms import ItemRelacionForm
from django.views.generic.edit import CreateView,  DeleteView
from django.views.generic import ListView
from gtg.forms import EliminarItemForm
from gtg.models import lineaBase
from gtg.forms import lbForm
from gtg.forms import ItemLbForm
from gtg.forms import CambioEstadoLbForm
from django.core.urlresolvers import reverse
from datetime import datetime
from gtg.forms import ComiteForm
from gtg.forms import EliminarRelacionItemForm
from gtg.models import SolicitudCambio
from gtg.forms import SolicitudCambioForm
from gtg.models import Voto
from gtg.forms import VotoForm
from gtg.forms import ComiteForm
from gtg.models import Archivo
from gtg.forms import ProyectoImportForm

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Indenter



def ingresar(request):
    """controla si el usuario se encuentra registrado, permite iniciar sesion
    \n@param request:
    \n@return retorna a la siguiente intefaz
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
@login_required(login_url='/ingresar')
def privado(request):
    """recibe un @param request con el cual permite acceder a la siguiente interfaz de modulos del proyecto
    \n@return a la interfaz principal"""
    usuario = request.user
    if(request.user.is_superuser):
        return HttpResponseRedirect('/proyectoAdmin')
    else:
        return HttpResponseRedirect('/proyecto')
    #return render_to_response('gestionProyecto.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    """funcion que cierra la sesion de un usuario registrado y logeado en el sistema, \nrecibe como @param un request
    y \n@return a la interfaz de inicio sesion"""
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/ingresar')
def administrar(request,codigoProyecto):
    proyecto= Proyectos.objects.get(pk=codigoProyecto)
    """permite acceder a la siguiente interfaz de modulo de administracion """
    return render(request, 'index2.html', {'proyecto': proyecto })


@login_required(login_url='/ingresar')
def desarrollo(request):
    """permite acceder a la siguiente interfaz de modulo de administracion"""
    return render_to_response('desarrollo.html',context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def configuracion(request):
    """permite acceder a la siguiente interfaz de modulo de administracion"""
    return render_to_response('configuracion.html',context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def usuario(request):
    """permite acceder a la interfaz de opciones de administracion para usuarios, \nrecibe un @param request, el cual
    es la peticion de acceso. Esta funcion muestra la lista de usuarios registrados en el sistema con ciertas operaciones
    a realizarse sobre ellos. \n@return la lista de usuarios en una tabla"""
    if request.user.is_superuser:
        usuarios=User.objects.all()
        usuario=Usuario.objects.all()
        usuariorol= RolUsuario.objects.all()
        return render_to_response('gestionUsuario.html', {'usuarios': usuarios, 'usuario': usuario, 'usuariorol': usuariorol }, context_instance=RequestContext(request))
    else:
        return render_to_response('extiende.html',context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def consultarUsuario(request, codigo):
    usuario= User.objects.get(pk= codigo)
    rol=RolUsuario.objects.all()
    return render(request, 'consultarUsuario.html', {'usuario': usuario , 'rol':rol})

@login_required(login_url='/ingresar')
def proyectoAdmin(request):
    """permite acceder a la interfaz de opciones de administracion para proyectos,\n recibe un @param request que es la
    peticion para realizar cierta operacion. \n@return retorna la lista de proyectos existentes en el sistema"""
    proyectos=Proyectos.objects.all()
    return render_to_response('gestionProyectoAdmin.html',{'proyectos': proyectos }, context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def proyecto(request):
    """permite acceder a la interfaz de opciones de administracion para proyectos, \nrecibe un @param request que es la
    peticion para realizar cierta operacion. \n@return retorna la lista de proyectos existentes en el sistema"""
    proyectos=Proyectos.objects.all()
    permisos= RolUsuario.objects.all()
    return render_to_response('gestionProyecto.html',{'proyectos': proyectos, 'permisos': permisos}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def fase(request):
   """permite acceder a la interfaz de opciones de administracion para fases"""
    #fases=Fases1.objects.all()
    #return render_to_response('gestionFase.html',{'fases': fases }, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def rolPermiso(request, mesagge= ""):
    """permite acceder a la interfaz de opciones de roles y permisos"""
    roles=Rol.objects.all()
    return render_to_response('gestionRolesPermisos.html', {'roles': roles, 'message': mesagge}, context_instance=RequestContext(request))



@login_required(login_url='/ingresar')
def lb(request, codigo):
    """permite acceder a la interfaz de opciones de administracion para linea base,\n recibe un @param request que es la
    peticion para realizar cierta operacion. \n@return retorna la lista de lineas base existentes en el proyecto"""
    linea=lineaBase.objects.filter(id=codigo)
    fa= Fases1.objects.get(pk=codigo)
    return render_to_response('gestionLB.html',{'lb': linea , 'fa': fa,'proyecto':fa.proyectos}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cambio(request,codigoProyecto):
    """permite acceder a la interfaz de opciones de administracion para Solicitudes de cambio"""
    proyecto=Proyectos.objects.get(pk=codigoProyecto)
    return render_to_response('gestionCambio.html',{'proyecto':proyecto},context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def registrarRol(request):
        """Permite registrar un nuevo rol en el sistema"""
	if request.method == "POST":
		formulario = rolForm(request.POST, request.FILES)

		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/rolPermiso')
	else:
		formulario=rolForm()
	return render(request, 'rol_form.html', {'formulario': formulario,})

@login_required(login_url='/ingresar')
def lista_roles(request, mesagge= ""):
        """Permite mostrar en pantalla todos los roles registrados en el sistema"""
	roles=Rol.objects.all()
	# return render(request, 'index.html', {'usuarios': usuarios,})
	return render_to_response('roles.html', {'roles': roles, 'message': mesagge}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def eliminar_rol(request, codigo):
    rol=Rol.objects.get(pk=codigo) # request.GET.get('codigo')
    rol.delete()
    return HttpResponseRedirect('/rolPermiso')

@login_required(login_url='/ingresar')
def nuevo_usuario(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/usuario')
        else:
            form= UserCreationForm()
        return render_to_response('altaUsuario.html', {'form':form}, context_instance=RequestContext(request))
    elif request.user.is_active:
        return render_to_response('extiende.html',context_instance=RequestContext(request))



@login_required(login_url='/ingresar')
def registrarProyecto(request):
    """Permite registrar un nuevo proyecto en el sistema. \nRecibe como @param un request que habilita
    el formulario para completar los datos del proyecto, una vez completado todos los campos obligatorios
    se crea el proyecto \ny @return a la interfaz proyecto, donde ya se visualiza en la lista el nuevo registro """
    b=1
    if request.user.is_superuser:
        if request.method == "POST":
		    formulario = ProyectoForm(request.POST, request.FILES)
		    if formulario.is_valid():
			    formulario.save()
			    return HttpResponseRedirect('/proyectoAdmin')
    	else:
            formulario=ProyectoForm()
        return render(request, 'proyecto_form.html', {'formulario': formulario,'b':b})
    elif request.user.is_active:
        return render_to_response('extiende.html',context_instance=RequestContext(request))


def buscarProyecto(request):
    '''
    vista para buscar los proyectos del sistema
    '''
    permisos= RolUsuario.objects.all()
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre=query)
        )
        resultados = Proyectos.objects.filter(qset).distinct()

    else:
        resultados = []


    return render_to_response('buscarProyecto.html', {'proyectos': resultados}, context_instance=RequestContext(request))

def importarProyecto(request, codigo):
    project = Proyectos.objects.get(pk=codigo)
    #print 'proyecto',project.nombre
    b=0
#    proyectos=Proyectos.objects.all()
 #   proyectoImport= Proyectos(fechaInicio = proyecto.fechaInicio,fechaFin= proyecto.fechaFin,fechaMod= proyecto.fechaMod,nombre = proyecto.nombre,complejidad= proyecto.complejidad,estado = proyecto.estado,lider= proyecto.lider)
    #proyectoImport= Proyectos('fechaInicio':proyecto.fechaInicio,'fechaFin': proyecto.fechaFin,'fechaMod': proyecto.fechaMod,'nombre': proyecto.nombre,'complejidad': proyecto.complejidad,'estado': proyecto.estado,'lider' proyecto.lider)

#    faseI=Fases1(fechaInicio=fase.fechaInicio,fechaFin=fase.fechaFin,nombre=fase.nombre,descripcion=fase.descripcion,estado=fase.estado)
    formulario = ProyectoForm(request.POST, initial={'fechaInicio':project.fechaInicio,'fechaFin': project.fechaFin,'complejidad': project.complejidad,'lider': project.lider} )
    #formulario = ProyectoForm(request.POST, instance=proyectoImport)
    if formulario.is_valid():
        formulario.save()
        HttpResponseRedirect('/proyecto')
        #return render_to_response('gestionFase1.html',{'fases': fases, 'proyecto':fase.proyectos}, context_instance=RequestContext(request))
    else:
        formulario = ProyectoForm(initial={'fechaInicio':project.fechaInicio,'fechaFin': project.fechaFin,'complejidad': project.complejidad,'lider': project.lider} )

        return render(request, 'proyecto_form.html', {'formulario': formulario,'b':b})




@login_required(login_url='/ingresar')
def lista_rolesModificar(request, mesagge= ""):
        """Permite mostrar en pantalla todos los roles registrados en el sistema"""
	roles=Rol.objects.all()
	# return render(request, 'index.html', {'usuarios': usuarios,})
	return render_to_response('rolesModificar.html', {'roles': roles, 'message': mesagge}, context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def editar(request, codigo):
        """Permite editar roles registrados en el sistema, \nrecibe como @param un request que es la peticion de la operacion y
        el codigo del rol a editar. \nRetorna @return el formulario con los datos a editar del rol en cuestion
        al aceptar la operacion,vuelve a la interfaz donde se despliega la lista de Roles registrados y modificados"""
	rol=Rol.objects.get(pk=codigo)
	if request.method == "POST":
		formulario = rolForm(request.POST, request.FILES, instance = rol)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/rolPermiso')

	else:
		formulario=rolForm(instance = rol)

	return render(request,'editar.html', {'formulario': formulario,})

@login_required(login_url='/ingresar')
def lista_proyectos(request):
	proyectos= Proyectos.objects.all()
	return render(request, 'lista_proyecto.html', {'proyectos': proyectos,})


######Vista de la lista de fases pertenecientes al proyecto selecionado##########
 ################################################################################
def fase1(request, codigoProyecto):
    """permite acceder a la interfaz de opciones de administracion para fases donde se despliega la lista de fases
    de cierto proyecto seleccionado.\n Recibe como @param request que es la peticion de la operacion y el codigo
    del proyecto, con el cual se filtra todas las fases pertenecientes al mismo. \n@return la lista de fases"""

    fases=Fases1.objects.filter(proyectos=codigoProyecto)
    proyecto= Proyectos.objects.get(pk=codigoProyecto)
    return render_to_response('gestionFase1.html',{'fases': fases, 'proyecto':proyecto }, context_instance=RequestContext(request))

#def fase(request):
#    """permite acceder a la interfaz de opciones de administracion para fases"""
#    fases=Fases1.objects.all()
#    return render_to_response('gestionFase.html',{'fases': fases }, context_instance=RequestContext(request))

#############################################################################################
####Vista del formulario para registrar una fase dentro del proyecto seleccinado#############
############################################################################################
@login_required(login_url='/ingresar')
def registrarFase(request,codigo):
    """
        Permite registrar una nueva fase dentro del proyecto en el sistema.\nRecibe como @param reuqest que es la peticion
	    de la operacion. \nRetorna @return el formulario con todos los campos para registrar una nueva fase. Al aceptar la
	    operacion vuevle a interfaz de fase donde se despliega la lista de fases actualmente registrados
	"""
    proyecto = Proyectos.objects.get(pk=codigo)
    proyecto.estado='ACT'
    proyecto.save()
    fase = Fases1(proyectos=proyecto)
    fases=Fases1.objects.all()
    formulario = Fases1Form(request.POST, instance=fase)
    if formulario.is_valid():
        formulario.save()
        return render_to_response('gestionFase1.html',{'fases': fases, 'proyecto':fase.proyectos }, context_instance=RequestContext(request))
    else:
        return render(request, 'fase_form.html', {'formulario': formulario,'proyecto':proyecto})



@login_required(login_url='/ingresar')
def editarUsuario(request, codigo):
    usuario= User.objects.get(pk= codigo)
    if request.method=="POST":
        formulario= UserCreationForm(request.POST, request.FILES, instance= usuario)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/usuario')
    else:
        formulario= UserCreationForm(instance=usuario)
    return render(request, 'modificarUsuario.html', {'formulario': formulario})

@login_required(login_url='/ingresar')
def lista_usuarios(request):
    usuarios= User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})



@login_required(login_url='/ingresar')
def editarFase(request, codigo):
        """Permite editar fases registradas en el sistema"""
	fases=Fases1.objects.all()
	fase=Fases1.objects.get(pk=codigo)

	if request.method == "POST":
		formulario = Fases1Form(request.POST, request.FILES, instance = fase)
		if formulario.is_valid():
			formulario.save()
			return render_to_response('gestionFase1.html',{'fases': fases, 'proyecto':fase.proyectos }, context_instance=RequestContext(request))


	else:
		formulario=Fases1Form(instance = fase)

	return render(request,'modificarFase.html', {'formulario': formulario,'proyecto':fase.proyectos})

@login_required(login_url='/ingresar')
def eliminar_fase(request, codigo):
    """"""
    fase=Fases1.objects.get(pk=codigo) # request.GET.get('codigo')
    return render_to_response('eliFase.html',{'fase':fase,'proyecto':fase.proyectos}, context_instance=RequestContext(request))

def eliFase(request, codigo):
    fase= Fases1.objects.get(pk=codigo)
    fases=Fases1.objects.all()
    fase.delete()
    return render_to_response('gestionFase1.html',{'fases': fases, 'proyecto':fase.proyectos }, context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def editarProyecto(request, codigo):
    """Permite editar proyectos registrados en el sistema"""
    if request.user.is_superuser:
        proyecto=Proyectos.objects.get(pk=codigo)
        if request.method == "POST":
		    formulario = ProyectoForm(request.POST, request.FILES, instance = proyecto)
		    if formulario.is_valid():
			    formulario.save()
			    return HttpResponseRedirect('/proyecto')
        else:
		    formulario=ProyectoForm(instance = proyecto)
        return render(request,'modificarProyecto.html', {'formulario': formulario})
    elif request.user.is_active:
        return render_to_response('extiende.html',context_instance=RequestContext(request))

def verProyecto(request, codigo):
        """Permite mostrar en pantalla todos los proyectos creados en el sistema"""
        if request.user.is_superuser:
            proyecto=Proyectos.objects.get(pk=codigo)
            return render_to_response('verProyecto.html', {'proyecto': proyecto}, context_instance=RequestContext(request))
        elif request.user.is_active:
            return render_to_response('extiende.html',context_instance=RequestContext(request))


################################################################################
###############Vista de Tipo de Atributo########################################
###############################################################################
@login_required(login_url='ingresar')
def tipoAtributo(request):
    """permite acceder a la interfaz de opciones de administracion para los tipos de atributos. \nRecibe @param request
    que es la peticion de la operacion. |nRetorna @return la lista de tipos de Atributos registrados actualmente en el sistema"""
    tAtributos= TipoAtributo.objects.all()
    return render_to_response('gestionAtributo.html',{'tAtributos': tAtributos}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def registrarTipoAtributo(request):
	"""Permite registrar un nuevo tipo de atributo dentro del proyecto en el sistema.\n Recibe como @param request que
	es la peticion de la operacion.\nRetorna @return el formulario con los campos a completar, se acepta la operacion
	y vuelve a la interfaz donde se despliega la lista de tipos atributos registrados en el sistema"""
	if request.method == "POST":
		formulario = TipoAtributoForm(request.POST, request.FILES)

		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/tipoAtributo')

	else:
		formulario=TipoAtributoForm()

	return render(request, 'fase_form.html', {'formulario': formulario,})

@login_required(login_url='/ingresar')
def editarUsuario(request, codigo):
    usuario= User.objects.get(pk= codigo)
    if request.method=="POST":
        formulario= UserCreationForm(request.POST, request.FILES, instance= usuario)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/usuario')
    else:
        formulario= UserCreationForm(instance=usuario)
    return render(request, 'modificarUsuario.html', {'formulario': formulario})

@login_required(login_url='/ingresar')
def consultarUsuario(request, codigo):
    usuario= User.objects.get(pk= codigo)
    rol=RolUsuario.objects.all()
    return render(request, 'consultarUsuario.html', {'usuario': usuario , 'rol':rol})

@login_required(login_url='/ingresar')
def lista_usuarios(request):
    usuarios= User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

@login_required(login_url='/ingresar')
def nuevo_rolusuario(request):
    """@param recibe un request como parametro, el cual es la operacion que permite acceder
     a un formulario con los cammpos de los datos de los usuarios y registra un nuevo usuario"""
    if request.method == 'POST':
        formulario = rolusuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect('/usuario')
    else:
        formulario= rolusuarioForm()
    return render_to_response('usuarioRol.html', {'formulario':formulario}, context_instance=RequestContext(request))



#@login_required(login_url='/ingresar')
#def editarFase(request, codigo):
 #       """Permite editar fases registradas en el sistemahdsjahda"""
#	fase=Fases1.objects.get(pk=codigo)
#	if request.method == "POST":
#		formulario = Fases1Form(request.POST, request.FILES, instance = fase)
#		if formulario.is_valid():
#			formulario.save()
#			return HttpResponseRedirect('/fase')
#
#	else:
#		formulario=Fases1Form(instance = fase)
#
#	return render(request,'modificarFase.html', {'formulario': formulario})


@login_required(login_url='/ingresar')
def lista_ProyectoEditar(request, mesagge= ""):
        """Permite mostrar en pantalla todos los proyectos creados en el sistema"""
	proyectos=Proyectos.objects.all()
	return render_to_response('lista_proyectoeditar.html', {'proyectos': proyectos, 'message': mesagge}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def editarProyecto(request, codigo):
    """Permite editar proyectos registrados en el sistema"""
    if request.user.is_superuser:
        proyecto=Proyectos.objects.get(pk=codigo)
        if request.method == "POST":
		    formulario = ProyectoForm(request.POST, request.FILES, instance = proyecto)
		    if formulario.is_valid():
			    formulario.save()
			    return HttpResponseRedirect('/proyecto')
        else:
		    formulario=ProyectoForm(instance = proyecto)
        return render(request,'modificarProyecto.html', {'formulario': formulario})
    elif request.user.is_active:
        return render_to_response('extiende.html',context_instance=RequestContext(request))

################################################################################
###############Vista de Tipo de Atributo########################################
###############################################################################
@login_required(login_url='ingresar')
def tipoAtributo(request):
    """permite acceder a la interfaz de opciones de administracion para los tipos de atributos. \nRecibe @param request
    que es la peticion de la operacion.\n Retorna @return la lista de tipos de Atributos registrados actualmente en el sistema"""
    tAtributos= TipoAtributo.objects.all()
    return render_to_response('gestionAtributo.html',{'tAtributos': tAtributos}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def registrarTipoAtributo(request):
	"""Permite registrar un nuevo tipo de atributo dentro del proyecto en el sistema.\n Recibe como @param request que
	es la peticion de la operacion.\nRetorna @return el formulario con los campos a completar, se acepta la operacion
	y vuelve a la interfaz donde se despliega la lista de tipos atributos registrados en el sistema"""
	if request.method == "POST":
		formulario = TipoAtributoForm(request.POST, request.FILES)

		if formulario.is_valid():
			#forma para poder ingresar a los datos del formulario, tal vez para hacer nuestras propias validaciones

			formulario.save()
			return HttpResponseRedirect('/tipoAtributo')

	else:
		formulario=TipoAtributoForm()

	return render(request, 'tipoAtributo_form.html', {'formulario': formulario,})

def modificar_tipoAtributo(request, codigo):
    """Permita modificar tipos de atributos registrados en el sistema, controla que el atributo en cuestion no este
    asociado a algun tipo de item.\n Recibe @param request, que es la peticion de la operacion y el codigo del tipo
    de atributo a modificar. \nRetorna @return a la interfaz de confirmacion de la operacion, esto es,despliega el
     formulario con todos los campos del tipo de atributo a modificar o de operacion denegada dependiendo de la
     relacion o no con el tipo de item. Al aceptar la operacion vuelve a la interfaz del listado de tipos de
     atributos existenes en el sistema"""

    ta= TipoAtributo.objects.get(pk=codigo)
    tipoItem= TipoItem.objects.all()
    for t in tipoItem:
        if t.tipoAtributo.id == ta.id:
            b=1
            return render_to_response('modTipoAtributo.html',{'t':t}, context_instance=RequestContext(request))

    tAtributo=TipoAtributo.objects.get(pk=codigo)

    if request.method == "POST":
        formulario = TipoAtributoForm(request.POST, request.FILES, instance = tAtributo)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/tipoAtributo')
    else:
        formulario=TipoAtributoForm(instance = tAtributo)
    return render(request,'modTipoAtributo1.html', {'formulario': formulario})

def eliminar_tipoAtributo(request, codigo):
    """Permita eliminar tipos de atributos registrados en el sistema, controla que el atributo en cuestion no este
    asociado a algun tipo de item. \nRecibe @param request, que es la peticion de la operacion y el codigo del tipo
    de atributo a eliminar. \nRetorna @return a la interfaz de confirmacion de la operacion o de operacion denegada
    dependiendo de la relacion o no con el tipo de item. Al aceptar la operacion vuelve a la interfaz del listado
    de tipo de atributos existenes en el sistema"""
    ta=TipoAtributo.objects.get(pk=codigo)
    tipoitem=TipoItem.objects.all()
    for ti in tipoitem:
        if ti.tipoAtributo.id == ta.id:
            return render_to_response('eliTipoAtributo.html',{'ti':ti}, context_instance=RequestContext(request))
    return render_to_response('eliTipoAtributo1.html',{'codigo':codigo}, context_instance=RequestContext(request))

def eliTipoAtributo(request, codigo):
    """Funcion que elimina un tipo de atributo que no este asociado a ningun tipo de item.\n Recibe @param un request,
    peticion de operacion, y el codigo del tipo de atributo a eliminar. Elimina el mismo \ny @return a la interfaz
    donde se despliega la lista de tipos de atributos existentes en el sistema."""
    tAtributo=TipoAtributo.objects.get(pk=codigo) # request.GET.get('codigo')
    tAtributo.delete()
    return HttpResponseRedirect('/tipoAtributo')

@login_required(login_url='/ingresar')
def tipoItem(request, codigoProyecto):
    """permite acceder a la interfaz  de tipo de Item, donde se despliega la lista de todos los tipos de items
    registrados en el sistema. \nRecibe un @param request, peticion de operacion y \n@return la lista"""
    tItem=TipoItem.objects.all()
    proyecto=Proyectos.objects.get(pk=codigoProyecto)
    return render_to_response('gestionTipoItem.html',{'tItem':tItem,'proyecto':proyecto},context_instance=RequestContext(request))

#@login_required(login_url='/ingresar')
#def registrarTipoItem(request, codigoProyecto):
#	"""Permite registrar un nuevo tipo de item a partir de un tipo de atributo dentro del proyecto en el sistema. \nRecibe como @param request que
#	es la peticion de la operacion.\nRetorna @return el formulario con los campos a completar, se acepta la operacion
#	y vuelve a la interfaz donde se despliega la lista de tipos de items registrados en el sistema"""
#	proyecto=Proyectos.objects.get(pk=codigoProyecto)
#	if request.method == "POST":
#		formulario = TipoItemForm(request.POST, request.FILES)
#
#		if formulario.is_valid():
#			formulario.save()
#			return HttpResponseRedirect('/tipoItem')
#
#	else:
#		formulario=TipoItemForm()
#
#	return render(request, 'tipoItem_form.html', {'formulario': formulario,'proyecto':proyecto})

############### Vista Item #####################################################
##############################################################################
@login_required(login_url='/ingresar')
@login_required(login_url='/ingresar')
def item(request, codigoProyecto):
    """permite acceder a la interfaz de Item, donde se despliega la lista de todos los items
    registrados en el sistema. Recibe un :param request, peticion de operacion y :return la lista"""
    indice=0
    proyecto=Proyectos.objects.get(pk=codigoProyecto)
    #nombre=dibujarProyecto(proyecto)
    items=Item.objects.all().order_by('nombre') #[:10]
    priori= Item.objects.all()
    for i in priori:
        for it in items:
            if(it.nombre==i.nombre ):
                it=i
    p=1
    return render_to_response('gestionItem.html',{'items':items,'p':p,'proyecto':proyecto},context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def registrarItem(request,codigo):
    """Permite registrar un nuevo item a partir de un tipo de item dentro del proyecto en el sistema. Recibe como :param request que
    es la peticion de la operacion.Retorna :return el formulario con los campos a completar, se acepta la operacion
    y vuelve a la interfaz donde se despliega la lista de items registrados en el sistema"""
    fase= Fases1.objects.get(pk=codigo)
    fase.estado='PEN'
    fase.save()
    item= Item(fase=fase)
    items=Item.objects.filter(fase=fase)
    formulario = ItemForm(request.POST, instance=item)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,
                         'El item "' + item.nombre + '" ha sido creado con exito')

        #return HttpResponseRedirect('/item')
        #guardar archivo
        if request.FILES.get('file')!=None:
            archivo=Archivo(archivo=request.FILES['file'],nombre='', item=codigo)
            archivo.save()

        return render_to_response('gestionItem1.html',{'items':items,'proyecto':fase.proyectos},context_instance=RequestContext(request))
    else:
        return render(request, 'item_form.html', {'formulario': formulario,'fase':fase})
@login_required(login_url='/ingresar')
def modificarItem(request, codigo):
    """Permita modificar item registrados en el sistema, controla que el item en cuestion este en un estado para
    ser modificado: REDAC o TER. Recibe :param request, que es la peticion de la operacion y el codigo del item
    a modificar. \nRetorna :return a la interfaz de confirmacion de la operacion, esto es,despliega el
     formulario con todos los campos del item a modificar. Al aceptar la operacion vuelve a la interfaz del listado
      items de existenes en el sistema"""
    items=Item.objects.all()
    item=Item.objects.get(pk=codigo)
    if request.method == "POST":
        formulario = ItemForm1(request.POST, request.FILES, instance = item)
        if formulario.is_valid():
            formulario.save()
            return render_to_response('gestionItem.html',{'items':items,'proyecto':item.fase.proyectos},context_instance=RequestContext(request))
    else:
        formulario=ItemForm1(instance = item)
    return render(request,'modificarItem.html', {'formulario': formulario,'proyecto':item.fase.proyectos})

@login_required(login_url='/ingresar')
def reversionarItem(request,codigo):
    it=Item.objects.all()
    item = Item.objects.get(pk=codigo)
    items=Item.objects.all()
    ultima_version=0
    priori=0
    relacionado=0
    for itm in it:
        if(itm.nombre==item.nombre and itm.version >= ultima_version):
            ultima_version=itm.version
        if(itm.nombre==item.nombre and itm.prioridad>= priori):
            priori=itm.prioridad

    itemR = Item( antecesorHorizontal=item.antecesorHorizontal,sucesorHorizontal=item.sucesorHorizontal,sucesorVertical=item.sucesorVertical,
            antecesorVertical=item.antecesorVertical,tipoItem=item.tipoItem,fase=item.fase,version=ultima_version+1, nombre=item.nombre, estado=item.estado,
            prioridad=priori+1)

    formulario = ItemReversionar(request.POST, instance=itemR)
    if request.method == "POST":
        formulario = ItemReversionar(request.POST, instance=itemR)
        if formulario.is_valid():
            formulario.save()
            return render_to_response('gestionItem.html',{'items':items,'proyecto':item.fase.proyectos},context_instance=RequestContext(request))
    else:
        formulario=ItemReversionar(request.POST, instance=itemR)
    return render(request,'item_form1.html', {'formulario': formulario,'item':item,'proyecto':item.fase.proyectos})


@login_required(login_url='/ingresar')
def relacionarItem(request, codigo,codigop):
    """Permite visualizar la lista de posibles items para relacionar a otro preciamente
     seleccionado
     \n@param request, que es la peticion de la operacion y el codigo del item
    a relacionar.\n Retorna @return a la interfaz de confirmacion de la operacion, esto es,despliega el
     formulario con las opciones de relacionar con un antecesor o sucesor del listado de items de existenes en el sistema"""

    item=Item.objects.get(pk=codigo)
    proyecto=Proyectos.objects.get(pk=codigop)
    fases=Fases1.objects.filter(proyectos=proyecto)
    items=Item.objects.all()
    return render(request,'listaRelacion.html', {'item': item,'items':items,'proyecto':proyecto,'fases':fases})

@login_required(login_url='/ingresar')
def relacItem(request, codigo,codigop):
    """Permite registrar un nuevo item a partir de un tipo de item dentro del proyecto en el sistema. \nRecibe como
    @param request que
    es la peticion de la operacion.Retorna \n@return el formulario con los campos a completar, se acepta la operacion
    y vuelve a la interfaz donde se despliega la lista de items registrados en el sistema"""
    item=Item.objects.get(pk=codigo)
    items=Item.objects.filter(fase=item.fase)
    itemRelacionado=Item.objects.get(pk=codigop)
    if (item.fase.id == itemRelacionado.fase.id):
        item.antecesorVertical=itemRelacionado
        item.antecesorVertical.relacon= 'ACT'
        item.antecesorHorizontal=None
    else:
        item.antecesorHorizontal=itemRelacionado
        item.antecesorHorizontal.relacion= 'ACT'
        item.antecesorVertical=None
    if request.method == "POST":

        formulario = relacionarForm(request.POST, request.FILES, instance = item)
        #formulario.fields['antecesorHorizontal'].queryset=Item.objects.filter(nombre='item1')
        if formulario.is_valid():
            formulario.save()
            return render_to_response('gestionItem1.html',{'items':items,'proyecto':item.fase.proyectos},context_instance=RequestContext(request))
    else:
        formulario=relacionarForm(instance = item)
    return render(request,'relacionarItems.html', {'formulario': formulario,'proyecto':item.fase.proyectos})







######Vista de la lista de items pertenecientes a la fase selecionada##########
 ################################################################################
@login_required(login_url='/ingresar')
def itemFase(request, codigo):
    """permite acceder a la interfaz de opciones de administracion para fases donde se despliega la lista de fases
    de cierto proyecto seleccionado. \nRecibe como @param request que es la peticion de la operacion y el codigo
    del proyecto, con el cual se filtra todas las fases pertenecientes al mismo. \n@return la lista de fases"""
    items=Item.objects.filter(fase=codigo)
    fase=Fases1.objects.get(pk=codigo)
    cantidad= 0
    for i in items:
        cantidad= cantidad +1
    return render_to_response('gestionItem1.html',{'items': items, 'fase':fase,'proyecto':fase.proyectos,'cantidad':cantidad }, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')

def itemTipoItem(request, codigo):
    """permite acceder a la interfaz de opciones de administracion para tipos de items donde se despliega la lista de fases
    de cierto proyecto seleccionado. Recibe como \n@param request que es la peticion de la operacion y el codigo
    del item, con el cual se filtra todas los tipos de item pertenecientes al mismo. \n@return la lista de items"""
    itemTipo=Item.objects.filter(tipoItem=codigo)
    item= Item.objects.get(pk=codigo)
    return render_to_response('gestionTipoItem1.html',{'itemTipo': itemTipo, 'item':item }, context_instance=RequestContext(request))

#@login_required(login_url='/ingresar')
@login_required(login_url='/ingresar')

def registrarTipoItem(request,codigoProyecto):
    """Permite registrar un nuevo tipo de item a partir de un tipo de atributo dentro del proyecto en el sistema.|n Recibe como @param request que
    es la peticion de la operacion.\nRetorna @return el formulario con los campos a completar, se acepta la operacion
    y vuelve a la interfaz donde se despliega la lista de tipos de items registrados en el sistema"""
    proyecto = Proyectos.objects.get(pk=codigoProyecto)
    tItem=TipoItem.objects.all()
    formulario = TipoItemForm(request.POST, request.FILES)
    if formulario.is_valid():
        formulario.save()
        return render_to_response('gestionTipoItem.html',{'proyecto':proyecto,'tItem':tItem }, context_instance=RequestContext(request))
    else:
        return render(request, 'tipoItem_form.html', {'formulario': formulario,'proyecto':proyecto})

@login_required(login_url='/ingresar')
def eliminarItem(request, codigo):
    """Funcion que elimina un tipo de atributo que no este asociado a ningun tipo de item. \nRecibe @param un request,
    peticion de operacion, y el codigo del tipo de atributo a eliminar. Elimina el mismo y\n @return a la interfaz
    donde se despliega la lista de tipos de atributos existentes en el sistema."""
    item= Item.objects.get(pk=codigo) # request.GET.get('codigo')
    return render_to_response('eliminarItem.html',{'item':item,'proyecto':item.fase.proyectos}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def eliItem(request, codigo):
    """Funcion que elimina un tipo de atributo que no este asociado a ningun tipo de item. \nRecibe @param un request,
    peticion de operacion, y el codigo del tipo de atributo a eliminar. Elimina el mismo y\n @return a la interfaz
    donde se despliega la lista de tipos de atributos existentes en el sistema."""
    item=Item.objects.get(pk=codigo)
    items=Item.objects.all()
    for i in items:
        if i.antecesorVertical == item:
            i.antecesorVertical.relacion= 'DEL'
            formAntecesor=EliminarRelacionItemForm(request.POST, instance=i)
            formAntecesor.save()
        if i.antecesorHorizontal == item:
            i.antecesorHorizontal.relacion= 'DEL'
            formAntecesor= EliminarRelacionItemForm(request.POST, instance=i)
            formAntecesor.save()
    item.estado='DESAC'
    if request.method == "POST":
        formulario = EliminarItemForm(request.POST, request.FILES, instance = item)
        if formulario.is_valid():
            formulario.save()
            return render_to_response('gestionItem.html',{'items':items,'proyecto':item.fase.proyectos},context_instance=RequestContext(request))
    else:
        formulario=EliminarItemForm(instance = item)
    return render(request,'eliminarItem1.html', {'formulario': formulario,'proyecto':item.fase.proyectos})

        #item.estado= 'Desactivado'
        #return HttpResponseRedirect('/item')
@login_required(login_url='/ingresar')
def revivirItem(request, codigo):
    """Funcion que revive un item eliminado. \nRecibe @param un request,
    peticion de operacion, y el codigo del item a revivir. Revive el mismo y\n @return a la interfaz
    donde se despliega la lista de items existentes en el sistema."""
    item=Item.objects.get(pk=codigo)
    items=Item.objects.all()
    for i in items:
        if i.antecesorVertical == item:
            i.antecesorVertical.relacion= 'ACT'
            formAntecesor=EliminarRelacionItemForm(request.POST, instance=i)
            formAntecesor.save()
        if i.antecesorHorizontal == item:
            i.antecesorHorizontal.relacion= 'ACT'
            formAntecesor= EliminarRelacionItemForm(request.POST, instance=i)
            formAntecesor.save()

    item.estado='REDAC'
    if request.method == "POST":
        formulario = EliminarItemForm(request.POST, request.FILES, instance = item)
        if formulario.is_valid():
            formulario.save()
            return render_to_response('gestionItem.html',{'items':items,'proyecto':item.fase.proyectos},context_instance=RequestContext(request))
    else:
        formulario=EliminarItemForm(instance = item)
    return render(request,'revivirItem.html', {'formulario': formulario})



    ################falta#######################################
@login_required(login_url='/ingresar')
def generarlb(request, codigo):
    """Permite generar una linea base dentro del proyecto en el sistema. \nRecibe como @param request que
    es la peticion de la operacion.\nRetorna @return el formulario con los campos a completar, se acepta la operacion
    y vuelve a la interfaz donde se despliega la lista de tipos de items registrados en el sistema"""
    fase= Fases1.objects.get(pk=codigo)

    lineaB= lineaBase(fase=fase)
    formulario = lbForm(request.POST, request.FILES, instance=lineaB)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/')
    else:
        formulario=lbForm(instance=lineaB)

	return render(request, 'lbForm.html', {'formulario': formulario, 'proyecto':fase.proyectos})

@login_required(login_url='/ingresar')
def listaItemsTer(request,codigo):
    """
    Lista todos los items con estado termina pertenecientes a cierta fase. \nRecibe como @param request peticion de la operacion
    y el codigo de la linea base en cuestion. \n Retorna @return a la intefaz con la lista de items solicitados
    """
    lb= lineaBase.objects.get(pk=codigo)
    items= Item.objects.filter(estado='TER')
    return render_to_response('listaItemTer.html', {'items': items, 'lb':lb,}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def relacionarItemLb(request, codigo, codigo1):
    """
    Relaciona cierto item a una linea base. \nRecibe como @param request, peticion de la operacion, el codigo del item a relacionar
    y el codigo de la linea base en cuestion. Genera la relacion \n Retorna @return a la intefaz para confirmar la operacion
    """
    item=Item.objects.get(pk=codigo1)

    lb = lineaBase.objects.get(id=codigo)
    fase= lb.fase
    fase.estado='ACT'
    fase.save()
    item.estado='VAL'
    item.lb=lineaBase.objects.get(id=codigo)

    #item = Item( lb=lb, estado='VAL')

    formulario = ItemLbForm(request.POST, instance= item)
    if formulario.is_valid():
        formulario.save()
        cantItem= Item.objects.filter(lb=lb)
        cantidad=0
        for ci in cantItem:
            cantidad= cantidad + 1

        if cantidad == item.fase.cantidadItem:
            lb.estado= 'CERRADA'
            lb.save()
        return HttpResponseRedirect('/')
    formulario= ItemLbForm(instance=item)
    return render(request,'ItemLb_form.html', {'formulario': formulario,})

@login_required(login_url='/ingresar')

def importarFase(request, codigo):
    fase = Fases1.objects.get(pk=codigo)
    fases=Fases1.objects.all()
    faseI=Fases1(fechaInicio=fase.fechaInicio,fechaFin=fase.fechaFin,nombre=fase.nombre,descripcion=fase.descripcion,estado=fase.estado,cantidadItem=fase.cantidadItem, orden=fase.orden)
    formulario = importarFaseForm(request.POST, instance=faseI)
    if formulario.is_valid():
        formulario.save()
        return render_to_response('gestionFase1.html',{'fases': fases, 'proyecto':fase.proyectos}, context_instance=RequestContext(request))
    else:
        return render(request, 'faseImport.html', {'formulario': formulario,'proyecto':fase.proyectos})

@login_required(login_url='/ingresar')

def finalizarFase(request, codigo):
    fase = Fases1.objects.get(pk=codigo)
    fases=Fases1.objects.all()
    formulario = finalizarFaseForm(request.POST, instance=fase)
    item= Item.objects.all()
    for i in item:
        if (i.fase== fase and i.estado!= 'VAL'):
            return render(request, 'faseNofinalizada.html', {'fase':codigo,'proyecto':fase.proyectos})
    fase.estado= 'FIN'
    if formulario.is_valid():
        formulario.save()
        return render_to_response('gestionFase1.html',{'fases': fases, 'proyecto':fase.proyectos }, context_instance=RequestContext(request))
    else:
        return render(request, 'faseImport.html', {'formulario': formulario,'fase':codigo,'proyecto':fase.proyectos})





@login_required(login_url='/ingresar')

def incluir_al_Comite(request,codigoProyecto):
    proyecto=Proyectos.objects.get(pk=codigoProyecto)
    if request.method == "POST":
        formulario = ComiteForm(request.POST, request.FILES, instance = proyecto)
        if formulario.is_valid():
            print ("=====================================")
            print (formulario.cleaned_data['comite'])
            print("========================================")
            formulario.save()
            return HttpResponseRedirect('/proyecto')
    else:
	    formulario=ComiteForm(instance = proyecto)
    return render(request,'comite.html', {'formulario': formulario})

#@login_required(login_url='/ingresar')

def recorridoProfundidad(item):
    """
    Funcion que llama a recorrer items en profundidad. \n recibe como @param el item en cuestion
    y\n retorna la suma del costo total del item.
    """
    fase=item.fase
    proyecto=fase.proyectos
    listaitems =itemsProyecto(proyecto)
    maxiditem = getMaxIdItemEnLista(listaitems)
    global sumaCosto, visitados
    visitados = [0]*(maxiditem+1)
    sumaCosto=0
    recorrer(item.id)
    return sumaCosto

def recorrer(id_item):
    """
    Funcion para recorrer el grafo de items del proyecto en profundidad
    Sumando el costo de cada uno
    """
    global sumaCosto, sumaTiempo, visitados
    visitados[id_item]=1
    item=Item.objects.get(id=id_item)
    sumaCosto = sumaCosto + item.prioridad
    relaciones = Item.objects.filter(antecesorVertical=item.id)
    for relacion in relaciones:
        if(visitados[relacion.id]==0):
            recorrer(relacion.id)



@login_required(login_url='/ingresar')
def crearSolicitudCambio(request,codigo):
    """
    Vista para la creacion de una solicitud de cambio para un item especificado
    \nRecibe como @param el request que es la peticion de la operacion y el id_item en cuestion
    \nRetorna @return al formulario para completar los datos de la solicitud para luego remitirlos
    a la lista de espera
    """
    item= Item.objects.get(pk= codigo)
    costototal= recorridoProfundidad(item)
    solicitud= SolicitudCambio(proyecto= item.fase.proyectos, item= item, costo= costototal, usuario= request.user)
    if request.method=='POST':
        formulario= SolicitudCambioForm(request.POST, instance= solicitud)
        if formulario.is_valid():
            solicitud.save()
            item.estado='REV'
            lb= item.lb
            lb.estado= 'REVISION'
            item.save()
            lb.save()
            return render_to_response('creacion_correcta.html',{'id_fase':item.fase.id}, context_instance=RequestContext(request))
    else:
        formulario=SolicitudCambioForm(instance= solicitud)
    return render_to_response('crear_solicitud.html',{'formulario':formulario, 'id_fase':item.fase.id}, context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def listaSolicitudes(request):

    """
    Vista para listar las solicitudes asignadas a un item expecifico
    \nRecibe como @param request, que es la peticion de la operacion
    \nRetorna @return la lista de todas las solicitudes de cambio de
    un item existenes dentro del proyecto
    """


    listaProyectos=Proyectos.objects.filter(comite=request.user.id)
    listaSolicitudes=[]
    if len(listaProyectos)==0:
        return render_to_response('listaSolicitudes.html', {'datos': listaSolicitudes}, context_instance=RequestContext(request))

    for proyecto in listaProyectos:
        lista= SolicitudCambio.objects.filter(proyecto=proyecto,estado= 'EN_ESPERA')
        for solicitud in lista:
            listaSolicitudes.append(solicitud)


    return render_to_response('listaSolicitudes.html', {'datos': listaSolicitudes}, context_instance=RequestContext(request))

#@login_required(login_url='/ingresar')

def puedeVotar(id_usuario,codigo):
    """
    Permite controlar que el usuario que intenta votar puede o no hacerlo, dependiendo si es miembro del comite o si ya habia votado
    \n Recibe como @param el id_usuario y id_solicitud
    \n Retorna @return True si aun no voto el usuario en cuestion y false en caso contrario
    """


    solicitud= SolicitudCambio.objects.get(id=codigo)
    proyecto= SolicitudCambio.objects.filter(proyecto= solicitud.proyecto)
    voto=Voto.objects.filter(usuario=id_usuario, solicitud=solicitud)
    if len(voto)!=0:
        return False
    else:
        return True


def getMaxIdItemEnLista(lista):
    """
    Funcion para hallar el id maximo de los items de una lista
    """
    max=0
    for item in lista:
        if item.id>max:
            max=item.id
    return max


def itemsProyecto(proyecto):
    """
    Funcion que recibe como @param un proyecto \ny retorna todos los items del mismo
    """
    fases = Fases1.objects.filter(proyectos=proyecto)
    items=[]
    for fase in fases:
        item=Item.objects.filter(fase=fase)
        for i in item:
            if i.estado!='DESAC':
                items.append(i)
    return items


def votar(request, codigo):
    """
    Vista que permite visualizar el formulario para iniciar la votacion para una solicitud especifica
    \nRecibe como @param request que es la peticion de la opercion y el id_solicitud en cuestion
    \nRetorna @return la intefaz de votacion exitosa o no dependiendo del caso
    """
    if puedeVotar(request.user.id, codigo)== False:
        return HttpResponseRedirect('/voto')

    solicitud= SolicitudCambio.objects.get(id=codigo)
    item=solicitud.item
    voto=Voto(solicitud=solicitud,usuario=request.user)

    if request.method=='POST':
        formulario=VotoForm(request.POST, instance= voto)
        if formulario.is_valid():
            formulario.save()
            votacionCerrada(solicitud)
            aprobada=2
            if votacionCerrada(solicitud):
                resultado(solicitud)
                if solicitud.estado=='APROBADA':
                    aprobada=1
                    #item.estado='REDAC'
                    #item.save()
                    listaitems =itemsProyecto(solicitud.proyecto)
                    maxiditem = getMaxIdItemEnLista(listaitems)
                    global nodos_visitados
                    nodos_visitados = [0]*(maxiditem+1)
                    estadoDependientes(item.id)
                    item.estado='REDAC'
                    item.save()

                    lb=item.lb
                    lb.estado='ROTA'
                    lb.save()
                else:
                    item.estado='VAL'
                    item.save()
                    lb= item.lb
                    lb.estado='CERRADA'
                    lb.save()
                    aprobada=0

            return render_to_response('votacionSatisfactoria.html',{'aprobada':aprobada}, context_instance=RequestContext(request))
    else:
        formulario=VotoForm(instance= voto)
    return render_to_response('votarSolicitud.html',{'formulario':formulario,'solicitud':solicitud}, context_instance=RequestContext(request))


def voto(request):
    """
    Vista para el acceso denegado en caso de que un usuario que no es miembro del comite desee votar o ya haya votado
    \nRecibe como @param request que es la peticion de la operacion
    \nRetorna @return a la interfaz segun sea el caso
    """

    usuario= request.user
    return render_to_response('accesoDenegado.html',{'usuario':usuario}, context_instance=RequestContext(request))

def votacionCerrada(solicitud):
    """
    Vista que permite controlar que todos los miembros del comite de cambio hayan votado para poder cerrar la votacion
    \nRecibe como @param la solicitud en cuestion
    \nRetorna @return True si la cantidad de votos coinciden con la cantidad de integrantes del comite, esto es si todos
    votaron y False en caso contrario
    """

    proyecto = SolicitudCambio.objects.filter(proyecto=solicitud.proyecto.id)
    voto=[]
    cant=0
    cantIntegrantes= solicitud.proyecto.comite.count()

    for miembro in solicitud.proyecto.comite.all():
        voto=Voto.objects.filter(usuario=miembro.id, solicitud=solicitud.id)
        if len(voto)==0:
            return False
        cant +=1
    if cant == cantIntegrantes:
        return True
    else:
        return False

def resultado(solicitud):
    """Vista que controla el resultado de las votaciones para saber si la solicitud fue aprobada o rechazado.
    \n Recibe como @param solicitud en cuestion,guarda el estado de la misma segun el caso.
    \n Retorna @return a la funcion votar"""

    votos = Voto.objects.filter(solicitud=solicitud.id)
    favor=0
    contra=0
    for voto in votos:
        if voto.voto=='RECHAZADO':
            contra+=1
        else:
            favor+=1

    if contra>favor:
        solicitud.estado='RECHAZADA'
    else:
        solicitud.estado='APROBADA'
        solicitud.fecha= datetime.now()
    solicitud.save()

def estadoDependientes(id_item):
    """
    Funcion para recorrer el grafo de items del proyecto en profundidad
    Sumando el costo y el tiempo de cada uno
    """
    global nodos_visitados
    nodos_visitados[id_item]=1

    item=Item.objects.get(id=id_item)
    #print item.estado
    if not(item.estado=='REDAC' or item.estado=='TER' or item.estado=='DESAC'):
        item.estado='REV'
        item.save()
        relaciones = Item.objects.filter(antecesorVertical=id_item)
        for relacion in relaciones:
            if(nodos_visitados[relacion.id]==0):
                estadoDependientes(relacion.id)



@login_required(login_url='/ingresar')
def consultarSolicitud(request,id_solicitud):
    """Vista que permite vizualizar los detalles de la solicitud de cambio especifico.
    \n Recibe como @param request, que es la peticion de la operacion y el id_solicitud en cuestion.
    \n Retorna @return a la interfaz que permite ver los detalles de la consulta"""

    solicitud= SolicitudCambio.objects.get(id=id_solicitud)
    votos = Voto.objects.filter(solicitud_id=solicitud.id)
    favor=0
    contra=0
    resultado=0
    usuarios=[]
    for voto in votos:
        usuarios.append(voto.usuario)
        if voto.voto=='RECHAZADO':
            contra+=1
        else:
            favor+=1
    if solicitud.estado == 'APROBADA':
        cant= solicitud.fecha - datetime.now()
        if cant+1 > 2:
            resultado=1

    return render_to_response('consultarSolicitud.html',{'usuarios':usuarios,'solicitud':solicitud, 'favor':favor, 'contra':contra, 'res':resultado}, context_instance=RequestContext(request))

def cambioEstadoLb(request, codigo):

    lBase= lineaBase.objects.get(pk=codigo)
    items= Item.objects.filter(lb=lBase)
    return render(request,'cambioEstadoLb.html', {'items': items,'lb':lBase})


@login_required(login_url='/ingresar')

def listaLbRota(request):
    """
    funcion que lista todas la lineas bases en estado rota.\nrecibe como @param request que es la peticion de la operacion
    \nreturn a la interfaz que lista dichas lineas bases
    """
    listaLbRota= lineaBase.objects.filter(estado='ROTA')
    return render_to_response('listaLbRota.html', {'datos': listaLbRota}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')

def listaItemRev(request, codigo):
    """
    funcion que lista los items que se encuentran en estado de revision \nrecibe como @param request que es la peticon de la operacion
    y el codigo de la linea base en cuestion\n @return la intefaz que lista dichos items
    """
    listaItems= Item.objects.filter(lb=codigo)
    return render_to_response('listaItemLbRota.html', {'datos': listaItems}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')

def historialCambio(request, codigo):
    """
    funcion que lista los items que se encuentran en cierta linea base.\n recibe como @param un requesr que es la peticion de la operacion
    y el codigo de la linea base en cuestion.\n @return la interfaz que lista dichos items
    """
    listaItems= Item.objects.filter(lb=codigo)
    return render_to_response('historialCambio.html', {'datos': listaItems}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')

def modificarItemVal(request, codigo):
    """Permita modificar item registrados en el sistema, controla que el item en cuestion este en un estado para
    ser modificado: REDAC o TER. Recibe :param request, que es la peticion de la operacion y el codigo del item
    a modificar. \nRetorna :return a la interfaz de confirmacion de la operacion, esto es,despliega el
     formulario con todos los campos del item a modificar. Al aceptar la operacion vuelve a la interfaz del listado
      items de existenes en el sistema"""
    items=Item.objects.all()
    item=Item.objects.get(pk=codigo)
    item.estado='VAL'
    lb= item.lb
    lb.estado= 'CERRADA'
    lb.save()
    if request.method == "POST":
        formulario = ItemFormVal(request.POST, request.FILES, instance = item)
        if formulario.is_valid():
            formulario.save()
                    #guardar archivo
            if request.FILES.get('file')!=None:
                archivo=Archivo(archivo=request.FILES['file'],nombre='', item=codigo)
                archivo.save()

            return render_to_response('gestionItem.html',{'items':items,'proyecto':item.fase.proyectos},context_instance=RequestContext(request))
    else:
        formulario=ItemFormVal(instance = item)
    return render(request,'modificarItemVal.html', {'formulario': formulario,'proyecto':item.fase.proyectos})

@login_required(login_url='/ingresar')

def consultarItem(request, codigo):
    """
    funcion que permite visualizar los detalles del item en cuestion.\n recibe como @param el request y el codigo del item
    \n @return la intefaz con los detalles del mismo
    """
    item= Item.objects.get(pk=codigo)
    return render_to_response('consultarItem.html', {'item': item}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')

def listaItemsProyecto(request, codigo):
    """
    funcion que lista los items pertenecientes a un proyecto en cuestion.\n recibe como @param el request y el codigo del proyecto
    \n@return la interfaz que lista dichos items
    """
    pro= Proyectos.objects.get(pk=codigo)

    items= itemsProyecto(pro)
    return render_to_response('listaItemsProyecto.html', {'items': items, 'proyecto': pro}, context_instance=RequestContext(request))

#@login_required(login_url='/ingresar')

def calcularImpacto(request, codigo):
    """
    funcion que calcula el impacto de un item en cuestion.\nrecibe como @param el request y el codigo del item.\n@return
    la interfaz con los detalles del impacto del item.
    """
    item= Item.objects.get(id=codigo)
    impacto= recorridoProfundidad(item)
    return render_to_response('calcularImpacto.html', {'item': item, 'impacto': impacto}, context_instance=RequestContext(request))
"""
def dibujarProyecto(proyecto):
    '''
    Funcion que grafica los items con sus relaciones de un proyecto dado
    '''
    #inicializar estructuras
    grafo = pydot.Dot(graph_type='digraph',fontname="Verdana",rankdir="LR")
    fases = Fases1.objects.filter(proyectos=proyecto).order_by('orden')
    clusters = []
    clusters.append(None)
    for fase in fases:
        if(fase.estado=='INA'):
            cluster = pydot.Cluster(str(fase.orden),
                                    label=str(fase.orden)+") "+fase.nombre,
                                    style="filled",
                                    fillcolor="gray")
        else:
            cluster = pydot.Cluster(str(fase.orden),
                                    label=str(fase.orden)+") "+fase.nombre)
        clusters.append(cluster)

    for cluster in clusters:
        if(cluster!=None):
            grafo.add_subgraph(cluster)


    lista=itemsProyecto(proyecto)
    items=[]
    for item in lista:
        if item.estado!="DESAC":
            items.append(item)
    #agregar nodos
    for item in items:

        if item.estado=="REDAC":
            clusters[item.fase.orden].add_node(pydot.Node(str(item.id),
                                                                 label=item.nombre,
                                                                 style="filled",
                                                                 fillcolor="yellow",
                                                                 fontcolor="white"))
        elif item.estado=="VAL":
            clusters[item.fase.orden].add_node(pydot.Node(str(item.id),
                                                                 label=item.nombre,
                                                                 style="filled",
                                                                 fillcolor="blue",
                                                                 fontcolor="white"))
        elif item.estado=="TER":
            clusters[item.fase.orden].add_node(pydot.Node(str(item.id),
                                                                 label=item.nombre,
                                                                 style="filled",
                                                                 fillcolor="green",
                                                                 fontcolor="white"))
        elif item.estado=="REV":
            clusters[item.fase.orden].add_node(pydot.Node(str(item.id),
                                                                 label=item.nombre,
                                                                 style="filled",
                                                                 fillcolor="red",
                                                                 fontcolor="white"))
        elif item.estado=="DESAC":
            clusters[item.fase.orden].add_node(pydot.Node(str(item.id),
                                                                 label=item.nombre,
                                                                 style="filled",
                                                                 fillcolor="magenta",
                                                                 fontcolor="white"))
    #agregar arcos
    for item in items:
        relaciones = Item.objects.filter(antecesorVertical=item).exclude(estado='DESAC')
        if relaciones!=None:
            for relacion in relaciones:
                grafo.add_edge(pydot.Edge(str(item.id),str(relacion.id),label='costo='+str(item.prioridad) ))

    date=datetime.now()

    name=str(date)+'grafico.jpg'
    grafo.write_jpg(str(settings.BASE_DIR)+'/gestograma/static/'+str(name))
    return name

"""

@login_required(login_url='/ingresar')

def reporte_usuarios():
    '''
    Funcion que genera el reporte de usuarios del sistema
    '''


    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/reporte_usuarios.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)

    Story=[]
    #logo = str(settings.BASE_DIR)+"/static/icono.png"
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=25, spaceBefore=15))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='SubItems',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=12,spaceAfter=10, spaceBefore=10))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
    #im = Image(logo, width=100,height=50)
    #Story.append(im)
    contador_act=1
    titulo="<b>Usuarios del Sistema<br/>"
    Story.append(Paragraph(titulo,styles['Principal']))


    Story.append(Spacer(1, 12))
    date=datetime.now()
    dateFormat = date.strftime("%d-%m-%Y")
    Story.append(Paragraph('Fecha: ' + str(dateFormat),styles['Subtitulos']))
    usuarios=User.objects.filter().order_by('is_active').reverse()
    usuarios_activos=User.objects.filter(is_active=True)
    cantidad_act=len(usuarios_activos)
    contador=-1
    titulo = Paragraph('<b>Usuarios Activos <\b>', styles['Titulo'])
    Story.append(Spacer(1, 12))
    Story.append(titulo)
    Story.append(Indenter(25))
    text ="__________________________________________________________<br>"
    Story.append(Paragraph(text, styles["Items"]))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))
    for usuario in usuarios:
            contador+=1
            if contador==cantidad_act:
                titulo = Paragraph('<b>Usuarios Inactivos <\b>', styles['Titulo'])
                Story.append(Spacer(1, 12))
                Story.append(titulo)
                contador_act=1
            Story.append(Indenter(25))
            text="<strong>"+str(contador_act)+".</strong>"
            Story.append(Paragraph(text, styles["Subtitulos"]))
            text ="<strong>Usuario: </strong>" + usuario.username +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Nombre: </strong>" + usuario.first_name + " "+ usuario.last_name +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>E-mail: </strong>" + usuario.email +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            dateFormat = usuario.date_joined.strftime("%d-%m-%Y %H:%M:%S")
            text ="<strong>Fecha de creacion: </strong>" + str(dateFormat) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            dateFormat = usuario.last_login.strftime("%d-%m-%Y %H:%M:%S")
            text ="<strong>Ultimo acceso: </strong>" + str(dateFormat) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Roles: </strong> <br>"
            Story.append(Paragraph(text, styles["Items"]))
            Story.append(Indenter(-25))
            #roles=Group.objects.filter(user__id=usuario.id)
            roles= Rol.objects.all()
            role= RolUsuario.objects.filter(usuario=usuario)
            for r in role:
                rol= Rol.objects.get(pk=r.rol.id)
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- " + rol.nombre +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
            Story.append(Indenter(25))
            text ="__________________________________________________________<br>"
            Story.append(Paragraph(text, styles["Items"]))
            Story.append(Spacer(1, 12))
            Story.append(Indenter(-25))
            contador_act+=1
    doc.build(Story)
    return str(settings.BASE_DIR)+"/reporte_usuarios.pdf"

@login_required(login_url='/ingresar')

def descargar_reporteUsuarios(request):
    '''
    Vista para descargar el reporte de lineas base de un proyecto especifico
    '''
    if request.user.is_superuser!=True:
        return HttpResponseRedirect('/denegado')
    a=file(reporte_usuarios())

    return StreamingHttpResponse(a,content_type='application/pdf')



def reporte_roles():
    '''
    Funcion que genera el reporte de roles del sistema
    '''


    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/reporte_roles.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)

    Story=[]
#    logo = str(settings.BASE_DIR)+"/static/icono.png"
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=25, spaceBefore=15))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='SubItems',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=12,spaceAfter=10, spaceBefore=10))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
 #   im = Image(logo, width=100,height=50)
  #  Story.append(im)
    contador_act=1
    titulo="<b>Roles del Sistema<br/>"
    Story.append(Paragraph(titulo,styles['Principal']))


    Story.append(Spacer(1, 12))
    date=datetime.now()
    dateFormat = date.strftime("%d-%m-%Y")
    Story.append(Paragraph('Fecha: ' + str(dateFormat),styles['Subtitulos']))
    roles= Rol.objects.all()
    Story.append(Indenter(25))
    text ="__________________________________________________________<br>"
    Story.append(Paragraph(text, styles["Items"]))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))
    for rol in roles:

            Story.append(Indenter(25))
            text="<strong>"+str(contador_act)+".</strong>"
            Story.append(Paragraph(text, styles["Subtitulos"]))
            text ="<strong>Nombre: </strong>" + rol.nombre +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Permisos <br></strong>"
            Story.append(Paragraph(text, styles["Items"]))
            if rol.controlTotal == True:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- controlTotal " + str(rol.controlTotal) +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
            if rol.aprobarItem == True:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- aprobarItem " + str(rol.aprobarItem) +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
            if rol.consultaItem == True:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- consultaItem " + str(rol.consultaItem) +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
            if rol.consultaLB == True:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- consultarLB " + str(rol.consultaLB) +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
            if rol.creacionLB == True:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- creacionLB " + str(rol.creacionLB) +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
            if rol.crearItem == True:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- crearItem " + str(rol.crearItem) +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
            if rol.eliminarItem == True:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- eliminarItem " + str(rol.eliminarItem) +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
            if rol.impactoItem == True:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- impactoItem" + str(rol.impactoItem) +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
            if rol.modificarItem == True:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- modificarItem " + str(rol.modificarItem) +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
            if rol.reversionarItem == True:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- reversionarItem " + str(rol.reversionarItem) +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))

            rolProyecto= RolUsuario.objects.filter(rol=rol)
            proyectos= Proyectos.objects.all()
            b=1
            text ="<strong>Proyectos asociados: </strong> <br>"
            Story.append(Paragraph(text, styles["Items"]))
            for rp in rolProyecto:
                p= Proyectos.objects.get(pk=rp.proyecto.id)
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- " + p.nombre + "<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
                b=0
            if b!= 0:
                text="<strong>Proyecto: </strong> Ninguno<br>"
                Story.append(Paragraph(text, styles["Items"]))
            Story.append(Indenter(-25))
            Story.append(Indenter(25))
            text ="__________________________________________________________<br>"
            Story.append(Paragraph(text, styles["Items"]))
            Story.append(Spacer(1, 12))
            Story.append(Indenter(-25))
            contador_act+=1
    doc.build(Story)
    return str(settings.BASE_DIR)+"/reporte_roles.pdf"

@login_required(login_url='/ingresar')

def descargar_reporteRoles(request):
    '''
    Vista para descargar el reporte de lineas base de un proyecto especifico
    '''
    if request.user.is_superuser!=True:
        return HttpResponseRedirect('/denegado')
    a=file(reporte_roles())

    return StreamingHttpResponse(a,content_type='application/pdf')



def reporte_proyectos():
    '''
    Funcion que genera el reporte de proyectos del sistema
    '''


    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/reporte_proyectos.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)


    Story=[]
#    logo = str(settings.BASE_DIR)+"/static/icono.png"
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=25, spaceBefore=15))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='SubsubsubItems',fontName='Helvetica',fontSize=8,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubsubItems',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubItems',fontName='Helvetica',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=14,spaceAfter=10, spaceBefore=10))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
 #   im = Image(logo, width=100,height=50)
  #  Story.append(im)
    contador_act=1
    titulo="<b>Proyectos del Sistema<br/>"
    Story.append(Paragraph(titulo,styles['Principal']))
    Story.append(Spacer(1, 12))
    date=datetime.now()
    dateFormat = date.strftime("%d-%m-%Y")
    Story.append(Paragraph('Fecha: ' + str(dateFormat),styles['Subtitulos']))
    proyectos_activos= Proyectos.objects.filter(estado='ACT')
    proyectos_fin=Proyectos.objects.filter(estado='FIN')
    proyectos_pen=Proyectos.objects.filter(estado='PEN')
    proyectos_anu=Proyectos.objects.filter(estado='ANU')
    proyectos=[]
    for p in proyectos_pen:
        proyectos.append(p)
    for p in proyectos_activos:
        proyectos.append(p)
    for p in proyectos_fin:
        proyectos.append(p)
    for p in proyectos_anu:
        proyectos.append(p)
    cantidad_pen=len(proyectos_pen)
    cantidad_act=len(proyectos_activos)
    cantidad_fin=len(proyectos_fin)
    contador1=0
    contador2=0
    contador3=0
    contador=0
    titulo = Paragraph('<b>Proyectos Pendientes <\b>', styles['Titulo'])
    Story.append(Spacer(1, 12))
    Story.append(titulo)
    Story.append(Indenter(25))
    text ="__________________________________________________________<br>"
    Story.append(Paragraph(text, styles["Items"]))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))
    for proyecto in proyectos:
            contador+=1
            if proyecto.estado=='ACT' and contador1==0:
                titulo = Paragraph('<b>Proyectos Activos <\b>', styles['Titulo'])
                Story.append(Spacer(1, 12))
                Story.append(titulo)
                contador1=1
                contador=1
            if proyecto.estado=='FIN' and contador2==0:
                titulo = Paragraph('<b>Proyectos Finalizados <\b>', styles['Titulo'])
                Story.append(Spacer(1, 12))
                Story.append(titulo)
                contador2=1
                contador=1
            if proyecto.estado=='ANU' and contador3==0:
                titulo = Paragraph('<b>Proyectos Anulados <\b>', styles['Titulo'])
                Story.append(Spacer(1, 12))
                Story.append(titulo)
                contador3=1
                contador=1

            Story.append(Indenter(25))
            text="<strong>"+str(contador)+".</strong>"
            Story.append(Paragraph(text, styles["Subtitulos"]))
            text ="<strong>Nombre: </strong>" + proyecto.nombre +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            dateFormat = proyecto.fechaInicio.strftime("%d-%m-%Y")
            text ="<strong>Fecha de inicio: </strong>" + str(dateFormat) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            dateFormat = proyecto.fechaFin.strftime("%d-%m-%Y")
            text ="<strong>Fecha de finalizacion: </strong>" + str(dateFormat) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Complejidad: </strong>" + str(proyecto.complejidad) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Lider: </strong>" + proyecto.lider.username +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Fases: </strong> <br>"
            Story.append(Paragraph(text, styles["SubItems"]))
            Story.append(Indenter(-25))
            fases=Fases1.objects.filter(proyectos   =proyecto)
            for fase in fases:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- " + fase.nombre +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
                items=Item.objects.filter(fase=fase)
                Story.append(Indenter(50))
                text ="<strong>Items: </strong> <br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))
                Story.append(Indenter(-50))
                for i in items:
                    text = ''
                    Story.append(Indenter(50))

                    text ="- " + i.nombre +"<br>"
                    Story.append(Paragraph(text, styles["SubsubItems"]))
                    Story.append(Indenter(-50))
                    tipos=TipoItem.objects.filter(tipoAtributo=i.tipoItem.tipoAtributo)
                    Story.append(Indenter(60))
                    text ="<strong>Tipos de Item: </strong> <br>"
                    Story.append(Paragraph(text, styles["SubsubsubItems"]))
                    Story.append(Indenter(-60))
                    for atributo in tipos:

                        text = ''
                        Story.append(Indenter(70))

                        text ="- " + atributo.nombre +"<br>"
                        Story.append(Paragraph(text, styles["SubsubItems"]))
                        Story.append(Indenter(-50))
                        Story.append(Indenter(60))
                        text ="<strong>Tipos de Atributo: </strong> <br>"
                        Story.append(Paragraph(text, styles["SubsubsubItems"]))
                        Story.append(Indenter(-60))


                        text = ''
                        Story.append(Indenter(70))
                        text ="- " + atributo.tipoAtributo.nombre + ", Tipo "+ atributo.tipoAtributo.tipo + "<br>"
                        Story.append(Paragraph(text, styles["SubsubsubItems"]))
                        Story.append(Indenter(-70))



            Story.append(Indenter(25))
            text ="__________________________________________________________<br>"
            Story.append(Paragraph(text, styles["Items"]))
            Story.append(Spacer(1, 12))
            Story.append(Indenter(-25))
            contador_act+=1
    doc.build(Story)
    return str(settings.BASE_DIR)+"/reporte_proyectos.pdf"

@login_required(login_url='/ingresar')

def descargar_reporteProyectos(request):
    '''
    Vista para descargar el reporte de lineas base de un proyecto especifico
    '''
    if request.user.is_superuser!=True:
        return HttpResponseRedirect('/denegado')
    a=file(reporte_proyectos())

    return StreamingHttpResponse(a,content_type='application/pdf')


def reporte_lineas_base(codigo):
    '''
    Funcion que recibe el id de un proyecto y genera un reporte en formato pdf de todas las lineas
    base que posee cada fase del proyecto, ordenado por fase y lineas bases con sus items
    '''

    fases=Fases1.objects.filter(proyectos=codigo).order_by('orden')
    proyecto = Proyectos.objects.get(id=codigo)
    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/reporte_lineasBase"+proyecto.nombre+".pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)

    Story=[]
#    logo = str(settings.BASE_DIR)+"/static/icono.png"
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=10, spaceBefore=15))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
 #   im = Image(logo, width=100,height=50)
  #  Story.append(im)
    titulo="<b>Lineas Base proyecto </b>"
    Story.append(Paragraph(titulo,styles['Principal']))


    Story.append(Spacer(1, 12))
    titulo="<b>" + proyecto.nombre+"</b>"
    Story.append(Paragraph(titulo,styles['Principal']))


    Story.append(Spacer(1, 12))
    date=datetime.now()
    dateFormat = date.strftime("%d-%m-%Y")
    Story.append(Paragraph('Fecha: ' + str(dateFormat),styles['Subtitulos']))
    for f in fases:
        Story.append(Spacer(1, 10))
        Story.append(Indenter(4))
        titulo = Paragraph('<b>' 'Fase  : '+ f.nombre + '<\b>', styles['Titulo'])
        Story.append(titulo)
        Story.append(Indenter(-4))

        lineasBase=set(lineaBase.objects.filter(fase=f))
        contador=0

        for lb in lineasBase:
            contador+=1

            ptext = str(contador)+ ". Linea Base" + "/" + lb.estado + " <br/>"

            Story.append(Indenter(15))
            Story.append(Spacer(1, 10))
            Story.append(Paragraph(ptext, styles["Justify"]))

            Story.append(Indenter(-15))
            if lb.estado=='CERRADA':
                items=Item.objects.filter(lb=lb)
            else:
                items=Item.objects.filter(lb=lb)
            ptext=''

            for item in items:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- " + item.nombre  +  ", Version: " + str(item.version)+"<br/"
                Story.append(Paragraph(text, styles["Items"]))
                Story.append(Indenter(-42))
    doc.build(Story)
    return str(settings.BASE_DIR)+"/reporte_lineasBase"+proyecto.nombre+".pdf"

@login_required
def descargar_reporteLB(request, codigo):
    '''
    Vista para descargar el reporte de lineas base de un proyecto especifico
    '''
    a=file(reporte_lineas_base(codigo))

    return StreamingHttpResponse(a,content_type='application/pdf')

def reporte_items(codigo):
    '''
    Funcion que genera el reporte de los items de un proyecto
    '''
    proyecto= Proyectos.objects.get(pk=codigo)
    fases=Fases1.objects.filter(proyectos=proyecto)
    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/reporte_items"+proyecto.nombre+".pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)


    Story=[]
#    logo = str(settings.BASE_DIR)+"/static/icono.png"
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=25, spaceBefore=3))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='SubsubsubItems',fontName='Helvetica',fontSize=8,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubsubItems',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubItems',fontName='Helvetica',fontSize=12,spaceAfter=10))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=14,spaceAfter=5, spaceBefore=5))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
 #   im = Image(logo, width=100,height=50)
  #  Story.append(im)
    contador_act=1
    titulo="<b>Items del Proyecto </b>"
    Story.append(Paragraph(titulo,styles['Principal']))
    Story.append(Spacer(1, 12))
    titulo="<b>" + proyecto.nombre+"<br/>"
    Story.append(Paragraph(titulo,styles['Principal']))
    Story.append(Spacer(1, 12))
    date=datetime.now()
    dateFormat = date.strftime("%d-%m-%Y")
    Story.append(Paragraph('Fecha: ' + str(dateFormat),styles['Subtitulos']))

    titulo = Paragraph('<b>Fases <\b>', styles['Titulo'])
    Story.append(Spacer(1, 12))
    Story.append(titulo)
    Story.append(Indenter(25))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))
    for fase in fases:
            Story.append(Indenter(25))
            text=""+str(fase.orden)+". "+fase.nombre+"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="______________________________________________<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Items: </strong> <br>"
            Story.append(Paragraph(text, styles["SubItems"]))
            Story.append(Indenter(-25))
            items=Item.objects.filter(fase=fase)
            for i in items:
                text = ''
                Story.append(Indenter(50))

                text ="<strong>Nombre: </strong>" + i.nombre +"<br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))
                Story.append(Indenter(-60))
                Story.append(Indenter(60))
                text ="<strong>Descripcion: </strong>"+i.descripcion+" <br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))
                text ="<strong>Costo: </strong>"+str(i.prioridad)+" <br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))
                text ="<strong>Estado: </strong>"+i.estado+" <br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))
                text ="<strong>Version: </strong>"+str(i.version)+" <br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))
                text ="<strong>Tipo de Item: </strong>"+i.tipoItem.nombre+" <br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))

                if i.antecesorVertical!=None:
                       #rel=get_object_or_404(Item,id=it.relacion_id)
                    text ="<strong>Relacion Vertical: </strong> "+i.nombre+" de "+i.antecesorVertical.nombre+"<br>"
                else:
                    text ="<strong>Relacion Horizontal: </strong> No tiene antecesor vertical<br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))
                if i.antecesorHorizontal!=None:
                       #rel=get_object_or_404(Item,id=it.relacion_id)
                    text ="<strong>Relacion Vertical: </strong> "+i.nombre+" de "+i.antecesorHorizontal.nombre+"<br>"
                else:
                    text ="<strong>Relacion Horizontal: </strong> No tiene antecesor horizontal<br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))

                dateFormat = i.fechaModi.strftime("%d-%m-%Y")
                text ="<strong>Fecha de creacion: </strong>"+dateFormat+" <br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))
                dateFormat = i.fechaModi.strftime("%d-%m-%Y")
                text ="<strong>Fecha de modificacion: </strong>"+dateFormat+" <br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))

                if i.lb!=None:
                    lb=lineaBase.objects.get(id=i.lb.id)
                    text ="<strong>Linea Base: </strong>"+str(lb.id)+" <br><br><br>"
                else:
                    text ="<strong>Linea Base: </strong> Ninguna <br><br><br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))
                Story.append(Indenter(-60))

    doc.build(Story)
    return str(settings.BASE_DIR)+"/reporte_items"+proyecto.nombre+".pdf"

@login_required(login_url='/ingresar')

def descargar_reporteItems(request, codigo):
    '''
    Vista para descargar el reporte de lineas base de un proyecto especifico
    '''
    a=file(reporte_items(codigo))

    return StreamingHttpResponse(a,content_type='application/pdf')


def reporte_solicitudes(codigo):
    '''
    Funcion que genera el reporte de roles del sistema
    '''

    proyecto = Proyectos.objects.get(pk=codigo)
    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/reporte_solicitudes"+proyecto.nombre+".pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)

    Story=[]
#    logo = str(settings.BASE_DIR)+"/static/icono.png"
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=25, spaceBefore=15))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='SubItems',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=12,spaceAfter=10, spaceBefore=10))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
 #   im = Image(logo, width=100,height=50)
  #  Story.append(im)
    contador_act=1
    titulo="<b>Solicitudes del proyecto </b>"
    Story.append(Paragraph(titulo,styles['Principal']))


    Story.append(Spacer(1, 12))
    titulo="<b>" +proyecto.nombre+ "</b>"
    Story.append(Paragraph(titulo,styles['Principal']))


    Story.append(Spacer(1, 12))
    date=datetime.now()
    dateFormat = date.strftime("%d-%m-%Y")
    Story.append(Paragraph('Fecha: ' + str(dateFormat),styles['Subtitulos']))
    solicitudes=[]
    solicitudesPen=SolicitudCambio.objects.filter(proyecto=proyecto,estado='EN_ESPERA')
    for s in solicitudesPen:
        solicitudes.append(s)
    pen=0
    solicitudesApr=SolicitudCambio.objects.filter(proyecto=proyecto,estado='APROBADA')
    for s in solicitudesApr:
        solicitudes.append(s)
    apr=0
    solicitudesRec=SolicitudCambio.objects.filter(proyecto=proyecto,estado='RECHAZADA')
    for s in solicitudesRec:
        solicitudes.append(s)
    rec=0
    contador=0
    for solicitud in solicitudes:

            contador+=1
            if solicitud.estado=='EN_ESPERA' and pen==0:
                titulo = Paragraph('<b>Solicitudes en Espera <\b>', styles['Titulo'])
                Story.append(Spacer(1, 12))
                Story.append(titulo)
                text ="__________________________________________________________<br>"
                Story.append(Paragraph(text, styles["Items"]))
                pen=1
                contador=1
            if solicitud.estado=='APROBADA' and apr==0:
                titulo = Paragraph('<b>Solicitudes Aprobadas <\b>', styles['Titulo'])
                Story.append(Spacer(1, 12))
                Story.append(titulo)
                text ="__________________________________________________________<br>"
                Story.append(Paragraph(text, styles["Items"]))
                apr=1
                contador=1

            if solicitud.estado=='RECHAZADA' and rec==0:
                titulo = Paragraph('<b>Solicitudes Rechazadas <\b>', styles['Titulo'])
                Story.append(Spacer(1, 12))
                Story.append(titulo)
                text ="__________________________________________________________<br>"
                Story.append(Paragraph(text, styles["Items"]))
                rec=1
                contador=1

            Story.append(Indenter(25))
            text="<strong>"+str(contador)+".</strong>"
            Story.append(Paragraph(text, styles["Subtitulos"]))
            text ="<strong>Nombre: </strong>" + solicitud.nombre +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Descripcion: </strong>" + solicitud.descripcion +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            it= Item.objects.get(pk=solicitud.item.id)
            text ="<strong>Item: </strong>" + it.nombre +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            dateFormat = solicitud.fecha.strftime("%d-%m-%Y")
            text ="<strong>Fecha de creacion: </strong>" + str(dateFormat) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Costo Total: </strong>" + str(solicitud.costo) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Usuario solicitante: </strong>" + solicitud.usuario.username +" "+ solicitud.usuario.last_name +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            favor=Voto.objects.filter(solicitud=solicitud,voto="APROBADO").count()
            contra=Voto.objects.filter(solicitud=solicitud,voto="RECHAZADO").count()
            text ="<strong>Votos a favor: </strong>" + str(favor) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Votos en contra: </strong>" + str(contra) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            Story.append(Spacer(1, 12))
            text ="__________________________________________________________<br>"
            Story.append(Paragraph(text, styles["Items"]))

            Story.append(Indenter(-25))


    doc.build(Story)
    return str(settings.BASE_DIR)+"/reporte_solicitudes"+proyecto.nombre+".pdf"

@login_required(login_url='/ingresar')

def descargar_reporteSolicitudes(request, codigo):
    '''
    Vista para descargar el reporte de solicitudes de un proyecto especifico
    '''
    a=file(reporte_solicitudes(codigo))

    return StreamingHttpResponse(a,content_type='application/pdf')