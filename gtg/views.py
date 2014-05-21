
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import User, UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from gtg.models import Usuario
from gtg.models import Rol
from gtg.models import Usuario
from gtg.forms import usuarioForm
from gtg.forms import rolForm
from gtg.forms import importarFaseForm
from gtg.forms import finalizarFaseForm

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
from gtg.models import ItemRelacion
from gtg.forms import ItemRelacionForm
from django.views.generic.edit import CreateView,  DeleteView
from django.views.generic import ListView
from gtg.forms import EliminarItemForm
from gtg.models import lineaBase
from gtg.forms import lbForm
from gtg.forms import ItemLbForm
from django.core.urlresolvers import reverse

from gtg.models import Comite
from gtg.forms import ComiteForm
from gtg.forms import EliminarRelacionItemForm
from gtg.models import Miembros

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

#@login_required(login_url='/ingresar')
#def fase(request):
 #   """permite acceder a la interfaz de opciones de administracion para fases"""
  #  fases=Fase.objects.all()
   # return render_to_response('gestionFase.html',{'fases': fases }, context_instance=RequestContext(request))

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
    if request.user.is_superuser:
        if request.method == "POST":
		    formulario = ProyectoForm(request.POST, request.FILES)
		    if formulario.is_valid():
			    formulario.save()
			    return HttpResponseRedirect('/proyectoAdmin')
    	else:
            formulario=ProyectoForm()
        return render(request, 'proyecto_form.html', {'formulario': formulario,})
    elif request.user.is_active:
        return render_to_response('extiende.html',context_instance=RequestContext(request))



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

    tipoItem= TipoItem.objects.all()
    for t in tipoItem:
        if t.tipoAtributo.id == codigo:
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
    tipoitem=TipoItem.objects.all()
    for ti in tipoitem:
        if ti.tipoAtributo.id == codigo:
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
    item= Item(fase=fase)
    items=Item.objects.all()
    formulario = ItemForm(request.POST, instance=item)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,
                         'El item "' + item.nombre + '" ha sido creado con exito')

        #return HttpResponseRedirect('/item')
        return render_to_response('gestionItem.html',{'items':items,'proyecto':fase.proyectos},context_instance=RequestContext(request))
    else:
        return render(request, 'item_form.html', {'formulario': formulario,'proyecto':fase.proyectos})

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


def relacItem(request, codigo,codigop):
    """Permite registrar un nuevo item a partir de un tipo de item dentro del proyecto en el sistema. \nRecibe como
    @param request que
    es la peticion de la operacion.Retorna \n@return el formulario con los campos a completar, se acepta la operacion
    y vuelve a la interfaz donde se despliega la lista de items registrados en el sistema"""
    item=Item.objects.get(pk=codigo)
    items=Item.objects.all()
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
            return render_to_response('gestionItem.html',{'items':items,'proyecto':item.fase.proyectos},context_instance=RequestContext(request))
    else:
        formulario=relacionarForm(instance = item)
    return render(request,'relacionarItems.html', {'formulario': formulario,'proyecto':item.fase.proyectos})







######Vista de la lista de items pertenecientes a la fase selecionada##########
 ################################################################################
def itemFase(request, codigo):
    """permite acceder a la interfaz de opciones de administracion para fases donde se despliega la lista de fases
    de cierto proyecto seleccionado. \nRecibe como @param request que es la peticion de la operacion y el codigo
    del proyecto, con el cual se filtra todas las fases pertenecientes al mismo. \n@return la lista de fases"""
    items=Item.objects.filter(fase=codigo)
    fase=Fases1.objects.get(pk=codigo)
    return render_to_response('gestionItem1.html',{'items': items, 'fase':fase,'proyecto':fase.proyectos }, context_instance=RequestContext(request))

#def itemTipoItem(request, codigo):
 #   """permite acceder a la interfaz de opciones de administracion para tipos de items donde se despliega la lista de fases
  #  de cierto proyecto seleccionado. Recibe como \n@param request que es la peticion de la operacion y el codigo
   # del item, con el cual se filtra todas los tipos de item pertenecientes al mismo. \n@return la lista de items"""
    #itemTipo=Item.objects.filter(tipoItem=codigo)
    #item= Item.objects.get(pk=codigo)
    #return render_to_response('gestionTipoItem1.html',{'itemTipo': itemTipo, 'item':item }, context_instance=RequestContext(request))

#@login_required(login_url='/ingresar')
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
    item.estado='VAL'
    item.lb=lineaBase.objects.get(id=codigo)
    #item = Item( lb=lb, estado='VAL')
    formulario = ItemLbForm(request.POST, instance= item)
    if formulario.is_valid():
		formulario.save()
		return HttpResponseRedirect('/')
    formulario= ItemLbForm(instance=item)
    return render(request,'ItemLb_form.html', {'formulario': formulario,})

def importarFase(request, codigo):
    fase = Fases1.objects.get(pk=codigo)
    fases=Fases1.objects.all()
    faseI=Fases1(fechaInicio=fase.fechaInicio,fechaFin=fase.fechaFin,nombre=fase.nombre,descripcion=fase.descripcion,estado=fase.estado)
    formulario = importarFaseForm(request.POST, instance=faseI)
    if formulario.is_valid():
        formulario.save()
        return render_to_response('gestionFase1.html',{'fases': fases, 'proyecto':fase.proyectos}, context_instance=RequestContext(request))
    else:
        return render(request, 'faseImport.html', {'formulario': formulario,'proyecto':fase.proyectos})

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
def comite(request,codigoProyecto):

    proyectoa= Proyectos.objects.get(pk=codigoProyecto)
#    comit=Comite.objects.get_or_create(proyecto=proyectoa)
    comite=Comite.objects.all()
    usuarios=User.objects.all()
    usuario=Usuario.objects.all()

    return render_to_response('comite.html', {'comite':comite,'proyecto':proyectoa,'usuarios': usuarios, 'usuario': usuario }, context_instance=RequestContext(request))



def incluir_al_Comite(request,codigoProyecto):
    proyecto=Proyectos.objects.get(pk=codigoProyecto)
    proyecto.cantIntegrantes=proyecto.cantIntegrantes+1
    if request.method == "POST":
		formulario = ComiteForm(request.POST, request.FILES, instance = proyecto)
		if formulario.is_valid():
			print "==============================================="
			print formulario.cleaned_data['comite']
			print "==============================================="
			formulario.save()
			return HttpResponseRedirect('/proyecto')
    else:
	    formulario=ComiteForm(instance = proyecto)
    return render(request,'modificarProyecto.html', {'formulario': formulario})


#    usuarios=User.objects.all()
#    proyectoR=Proyectos.objects.get(pk=codigoProyecto)
#    usuarioR=User.objects.get(pk=codigoUsuario)
        #comit=Comite.objects.get(proyecto=proyectoR)
        #comit.cantidad_integrantes=comit.cantidad_integrantes+1
        #comit.usuario=usuarioR
        #comit.proyecto=proyectoR
#    cont=0
#    cmt=Comite.objects.all()
#    for c in cmt:
#        if(c.proyecto==proyectoR):
#            cont=cont+1

#    comit=Comite(proyecto=proyectoR,usuario=usuarioR,cantidad_integrantes=cont+1)
#    if request.method == "POST":
#        formulario = ComiteForm(request.POST, request.FILES,instance=comit)
#        if formulario.is_valid():
#            formulario.save()
#            return render_to_response('comite.html', {'comite':comit,'proyecto':proyectoR,'usuarios': usuarios}, context_instance=RequestContext(request))
#    else:
#        formulario=ComiteForm(instance = comit)
#    return render(request,'nuevoIntegrante.html', {'formulario': formulario,'proyecto':proyectoR})


