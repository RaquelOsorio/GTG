
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
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
import os
from os.path import join,realpath
from django.conf import settings
from gtg.forms import rolusuarioForm
from gtg.models import RolUsuario
from django.shortcuts import render_to_response

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

from gtg.forms import ItemForm1
from gtg.models import ItemRelacion
from gtg.forms import ItemRelacionForm
from django.views.generic.edit import CreateView,  DeleteView
from django.views.generic import ListView
from gtg.forms import EliminarItemForm
from gtg.models import lineaBase
from gtg.forms import lbForm
from django.core.urlresolvers import reverse

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
@login_required(login_url='/ingresar')
def privado(request):
    """recibe un :param request con el cual permite acceder a la siguiente interfaz de modulos del proyecto
    :return a la interfaz principal"""
    usuario = request.user
    if(request.user.is_superuser):
        return HttpResponseRedirect('/proyectoAdmin')
    else:
        return HttpResponseRedirect('/proyecto')
    #return render_to_response('gestionProyecto.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    """funcion que cierra la sesion de un usuario registrado y logeado en el sistema, recibe como :param un request
    y :return a la interfaz de inicio sesion"""
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/ingresar')
def administrar(request):

    """permite acceder a la siguiente interfaz de modulo de administracion """
    return render_to_response('prueba.html',context_instance=RequestContext(request))


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
    """permite acceder a la interfaz de opciones de administracion para usuarios, recibe un :param request, el cual
    es la peticion de acceso. Esta funcion muestra la lista de usuarios registrados en el sistema con ciertas operaciones
    a realizarse sobre ellos. :return la lista de usuarios en una tabla"""
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
    """permite acceder a la interfaz de opciones de administracion para proyectos, recibe un :param request que es la
    peticion para realizar cierta operacion. :return retorna la lista de proyectos existentes en el sistema"""
    proyectos=Proyectos.objects.all()
    return render_to_response('gestionProyectoAdmin.html',{'proyectos': proyectos }, context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def proyecto(request):
    """permite acceder a la interfaz de opciones de administracion para proyectos, recibe un :param request que es la
    peticion para realizar cierta operacion. :return retorna la lista de proyectos existentes en el sistema"""
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
def item(request):
    """permite acceder a la interfaz de opciones de administracion para items"""
    return render_to_response('gestionItem.html',context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def lb(request, codigoFase):
    """permite acceder a la interfaz de opciones de administracion para linea base, recibe un :param request que es la
    peticion para realizar cierta operacion. :return retorna la lista de lineas base existentes en el proyecto"""
    linea=lineaBase.objects.filter(id=codigoFase)
    return render_to_response('gestionLB.html',{'lb': linea , 'fase': codigoFase}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cambio(request):
    """permite acceder a la interfaz de opciones de administracion para Solicitudes de cambio"""
    return render_to_response('gestionCambio.html',context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
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
    """Permite registrar un nuevo proyecto en el sistema. Recibe como :param un request que habilita
    el formulario para completar los datos del proyecto, una vez completado todos los campos obligatorios
    se crea el proyecto y regresa a la interfaz proyecto, donde ya se visualiza en la lista el nuevo registro """
    if request.user.is_superuser:
        if request.method == "POST":
		    formulario = ProyectoForm(request.POST, request.FILES)
		    if formulario.is_valid():
			    #forma para poder ingresar a los datos del formulario, tal vez para hacer nuestras propias validaciones
			    print "==============================================="
			    print formulario.cleaned_data['nombre']
			    print "==============================================="
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
        """Permite editar roles registrados en el sistema, recibe como :param un request que es la peticion de la operacion y
        el codigo del rol a editar. Retorna :return el formulario con los datos a editar del rol en cuestion
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
def fase1(request, codigo):
    """permite acceder a la interfaz de opciones de administracion para fases donde se despliega la lista de fases
    de cierto proyecto seleccionado. Recibe como :param request que es la peticion de la operacion y el codigo
    del proyecto, con el cual se filtra todas las fases pertenecientes al mismo. :return la lista de fases"""

    fases=Fases1.objects.filter(proyectos=codigo)
    return render_to_response('gestionFase1.html',{'fases': fases, 'proyecto':codigo }, context_instance=RequestContext(request))

def fase(request):
    """permite acceder a la interfaz de opciones de administracion para fases"""
    fases=Fases1.objects.all()
    return render_to_response('gestionFase.html',{'fases': fases }, context_instance=RequestContext(request))

#############################################################################################
####Vista del formulario para registrar una fase dentro del proyecto seleccinado#############
############################################################################################
@login_required(login_url='/ingresar')
def registrarFase(request,codigo):
    """
        Permite registrar una nueva fase dentro del proyecto en el sistema.Recibe como :param reuqest que es la peticion
	    de la operacion. Retorna :return el formulario con todos los campos para registrar una nueva fase. Al aceptar la
	    operacion vuevle a interfaz de fase donde se despliega la lista de fases actualmente registrados
	"""
    proyecto = Proyectos.objects.get(pk=codigo)
    fase = Fases1(proyectos=proyecto)
    formulario = Fases1Form(request.POST, instance=fase)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/fase')
    else:
        return render(request, 'fase_form.html', {'formulario': formulario})

    """proy=RolUsuario.objects.all()
    request.POST=request.POST.copy()
    request.POST.__setitem__('proyecto',codigo)
    proyecto=Proyectos.objects.get(pk=codigo)
    form = Fases1Form(request.POST or None)
    if request.method == "POST":
        formulario = Fases1Form(request.POST, request.FILES)
        if formulario.is_valid():
		    #forma para poder ingresar a los datos del formulario, tal vez para hacer nuestras propias validaciones
            print "==============================================="
            print formulario.cleaned_data['nombre']
            print "==============================================="
            f = Fases1(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'],proyectos=proyecto,)

            formulario.save()
            return HttpResponseRedirect('/fase')
    else:
        formulario=Fases1Form()

	return render(request, 'fase_form.html', {'formulario': formulario,'proy':proy})
    """

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
	fase=Fases1.objects.get(pk=codigo)
	if request.method == "POST":
		formulario = Fases1Form(request.POST, request.FILES, instance = fase)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/fase')

	else:
		formulario=Fases1Form(instance = fase)

	return render(request,'modificarFase.html', {'formulario': formulario})

@login_required(login_url='/ingresar')
def eliminar_fase(request, codigo):
    """"""
    fase=Fases1.objects.get(pk=codigo) # request.GET.get('codigo')
    return render_to_response('eliFase.html',{'fase':fase}, context_instance=RequestContext(request))

def eliFase(request, codigo):
    fase= Fases1.objects.get(pk=codigo)
    fase.delete()
    return HttpResponseRedirect('/fase')

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
    """permite acceder a la interfaz de opciones de administracion para los tipos de atributos. Recibe :param request
    que es la peticion de la operacion. Retorna :return la lista de tipos de Atributos registrados actualmente en el sistema"""
    tAtributos= TipoAtributo.objects.all()
    return render_to_response('gestionAtributo.html',{'tAtributos': tAtributos}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def registrarTipoAtributo(request):
	"""Permite registrar un nuevo tipo de atributo dentro del proyecto en el sistema. Recibe como :param request que
	es la peticion de la operacion.Retorna :return el formulario con los campos a completar, se acepta la operacion
	y vuelve a la interfaz donde se despliega la lista de tipos atributos registrados en el sistema"""
	if request.method == "POST":
		formulario = TipoAtributoForm(request.POST, request.FILES)

		if formulario.is_valid():
			#forma para poder ingresar a los datos del formulario, tal vez para hacer nuestras propias validaciones
			print "==============================================="
			print formulario.cleaned_data['nombre']
			print "==============================================="
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
    """:param recibe un request como parametro, el cual es la operacion que permite acceder
     a un formulario con los cammpos de los datos de los usuarios y registra un nuevo usuario"""
    if request.method == 'POST':
        formulario = rolusuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect('/usuario')
    else:
        formulario= rolusuarioForm()
    return render_to_response('usuarioRol.html', {'formulario':formulario}, context_instance=RequestContext(request))



@login_required(login_url='/ingresar')
def editarFase(request, codigo):
        """Permite editar fases registradas en el sistema"""
	fase=Fases1.objects.get(pk=codigo)
	if request.method == "POST":
		formulario = Fases1Form(request.POST, request.FILES, instance = fase)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/fase')

	else:
		formulario=Fases1Form(instance = fase)

	return render(request,'modificarFase.html', {'formulario': formulario})


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
    """permite acceder a la interfaz de opciones de administracion para los tipos de atributos. Recibe :param request
    que es la peticion de la operacion. Retorna :return la lista de tipos de Atributos registrados actualmente en el sistema"""
    tAtributos= TipoAtributo.objects.all()
    return render_to_response('gestionAtributo.html',{'tAtributos': tAtributos}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def registrarTipoAtributo(request):
	"""Permite registrar un nuevo tipo de atributo dentro del proyecto en el sistema. Recibe como :param request que
	es la peticion de la operacion.Retorna :return el formulario con los campos a completar, se acepta la operacion
	y vuelve a la interfaz donde se despliega la lista de tipos atributos registrados en el sistema"""
	if request.method == "POST":
		formulario = TipoAtributoForm(request.POST, request.FILES)

		if formulario.is_valid():
			#forma para poder ingresar a los datos del formulario, tal vez para hacer nuestras propias validaciones
			print "==============================================="
			print formulario.cleaned_data['nombre']
			print "==============================================="
			formulario.save()
			return HttpResponseRedirect('/tipoAtributo')

	else:
		formulario=TipoAtributoForm()

	return render(request, 'tipoAtributo_form.html', {'formulario': formulario,})

def modificar_tipoAtributo(request, codigo):
    """Permita modificar tipos de atributos registrados en el sistema, controla que el atributo en cuestion no este
    asociado a algun tipo de item. Recibe :param request, que es la peticion de la operacion y el codigo del tipo
    de atributo a modificar. Retorna :return a la interfaz de confirmacion de la operacion, esto es,despliega el
     formulario con todos los campos del tipo de atributo a modificar o de operacion denegada dependiendo de la
     relacion o no con el tipo de item. Al aceptar la operacion vuelve a la interfaz del listado de tipos de
     atributos existenes en el sistema"""

    tipoItem= TipoItem.objects.all()
    for t in tipoItem:
        if t.tipoAtributo.id == codigo:
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
    asociado a algun tipo de item. Recibe :param request, que es la peticion de la operacion y el codigo del tipo
    de atributo a eliminar. Retorna :return a la interfaz de confirmacion de la operacion o de operacion denegada
    dependiendo de la relacion o no con el tipo de item. Al aceptar la operacion vuelve a la interfaz del listado
    de tipo de atributos existenes en el sistema"""
    tipoitem=TipoItem.objects.all()
    for ti in tipoitem:
        if ti.tipoAtributo.id == codigo:
            return render_to_response('eliTipoAtributo.html',{'ti':ti}, context_instance=RequestContext(request))
    return render_to_response('eliTipoAtributo1.html',{'codigo':codigo}, context_instance=RequestContext(request))

def eliTipoAtributo(request, codigo):
    """Funcion que elimina un tipo de atributo que no este asociado a ningun tipo de item. Recibe :param un request,
    peticion de operacion, y el codigo del tipo de atributo a eliminar. Elimina el mismo y :return a la interfaz
    donde se despliega la lista de tipos de atributos existentes en el sistema."""
    tAtributo=TipoAtributo.objects.get(pk=codigo) # request.GET.get('codigo')
    tAtributo.delete()
    return HttpResponseRedirect('/tipoAtributo')

@login_required(login_url='/ingresar')
def tipoItem(request):
    """permite acceder a la interfaz  de tipo de Item, donde se despliega la lista de todos los tipos de items
    registrados en el sistema. Recibe un :param request, peticion de operacion y :return la lista"""
    tItem=TipoItem.objects.all()
    return render_to_response('gestionTipoItem.html',{'tItem':tItem},context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def registrarTipoItem(request):
	"""Permite registrar un nuevo tipo de item a partir de un tipo de atributo dentro del proyecto en el sistema. Recibe como :param request que
	es la peticion de la operacion.Retorna :return el formulario con los campos a completar, se acepta la operacion
	y vuelve a la interfaz donde se despliega la lista de tipos de items registrados en el sistema"""
	if request.method == "POST":
		formulario = TipoItemForm(request.POST, request.FILES)

		if formulario.is_valid():
			#forma para poder ingresar a los datos del formulario, tal vez para hacer nuestras propias validaciones
			print "==============================================="
			print formulario.cleaned_data['nombre']
			print "==============================================="
			formulario.save()
			return HttpResponseRedirect('/tipoItem')

	else:
		formulario=TipoItemForm()

	return render(request, 'tipoItem_form.html', {'formulario': formulario,})

############### Vista Item #####################################################
##############################################################################
@login_required(login_url='/ingresar')
def item(request):
    """permite acceder a la interfaz de Item, donde se despliega la lista de todos los items
    registrados en el sistema. Recibe un :param request, peticion de operacion y :return la lista"""
    items=Item.objects.all()
    return render_to_response('gestionItem.html',{'items':items},context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def registrarItem(request):
	"""Permite registrar un nuevo item a partir de un tipo de item dentro del proyecto en el sistema. Recibe como :param request que
	es la peticion de la operacion.Retorna :return el formulario con los campos a completar, se acepta la operacion
	y vuelve a la interfaz donde se despliega la lista de items registrados en el sistema"""
	if request.method == "POST":
		formulario = ItemForm(request.POST, request.FILES)

		if formulario.is_valid():
			#forma para poder ingresar a los datos del formulario, tal vez para hacer nuestras propias validaciones
			print "==============================================="
			print formulario.cleaned_data['nombre']
			print "==============================================="
			formulario.save()
			return HttpResponseRedirect('/item')

	else:
		formulario=ItemForm()

	return render(request, 'item_form.html', {'formulario': formulario,})

def modificarItem(request, codigo):
    """Permita modificar item registrados en el sistema, controla que el item en cuestion este en un estado para
    ser modificado: REDAC o TER. Recibe :param request, que es la peticion de la operacion y el codigo del item
    a modificar. \nRetorna :return a la interfaz de confirmacion de la operacion, esto es,despliega el
     formulario con todos los campos del item a modificar. Al aceptar la operacion vuelve a la interfaz del listado
      items de existenes en el sistema"""

    item=Item.objects.get(pk=codigo)
    if request.method == "POST":
        formulario = ItemForm1(request.POST, request.FILES, instance = item)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/item')
    else:
        formulario=ItemForm1(instance = item)
    return render(request,'modificarItem.html', {'formulario': formulario})


def reversionarItem(request, codigo):
    it=Item.objects.all()
    item = Item.objects.get(pk=codigo)
    itemR = Item( antecesorHorizontal=item.antecesorHorizontal,sucesorHorizontal=item.sucesorHorizontal,sucesorVertical=item.sucesorVertical,antecesorVertical=item.antecesorVertical,tipoItem=item.tipoItem,fase=item.fase,version=item.version+1, nombre=item.nombre, estado=item.estado, prioridad=item.prioridad, descripcion=item.descripcion)
    formulario = ItemReversionar(request.POST, instance=itemR)
    if formulario.is_valid():
        formulario.save()
        return render(request, 'item_form1.html', {'formulario': formulario,"it":it,"item":item})
    else:
        return render(request, 'item_form1.html', {'formulario': formulario,"it":it,"item":item})



def relacionarItem(request, codigo):
    """Permita relacionar items registrados en el sistema, controla que el item en cuestion este en un estado para
    ser modificado: REDAC o TER. Recibe :param request, que es la peticion de la operacion y el codigo del item
    a modificar. Retorna :return a la interfaz de confirmacion de la operacion, esto es,despliega el
     formulario con las opciones de relacionar con un antecesor o sucesor del listado de items de existenes en el sistema"""

    item=Item.objects.get(pk=codigo)
    if request.method == "POST":
        formulario = relacionarForm(request.POST, request.FILES, instance = item)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/item')
    else:
        formulario=relacionarForm(instance = item)
    return render(request,'relacionarItem.html', {'formulario': formulario})

######Vista de la lista de items pertenecientes a la fase selecionada##########
 ################################################################################
def itemFase(request, codigo):
    """permite acceder a la interfaz de opciones de administracion para fases donde se despliega la lista de fases
    de cierto proyecto seleccionado. Recibe como :param request que es la peticion de la operacion y el codigo
    del proyecto, con el cual se filtra todas las fases pertenecientes al mismo. :return la lista de fases"""
    items=Item.objects.filter(fase=codigo)
    return render_to_response('gestionItem1.html',{'items': items }, context_instance=RequestContext(request))

def itemTipoItem(request, codigo):
    """permite acceder a la interfaz de opciones de administracion para fases donde se despliega la lista de fases
    de cierto proyecto seleccionado. Recibe como :param request que es la peticion de la operacion y el codigo
    del proyecto, con el cual se filtra todas las fases pertenecientes al mismo. :return la lista de fases"""
    itemTipo=Item.objects.filter(tipoItem=codigo)
    return render_to_response('gestionTipoItem1.html',{'itemTipo': itemTipo }, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def registrarTipoItem(request):
	"""Permite registrar un nuevo tipo de item a partir de un tipo de atributo dentro del proyecto en el sistema. Recibe como :param request que
	es la peticion de la operacion.Retorna :return el formulario con los campos a completar, se acepta la operacion
	y vuelve a la interfaz donde se despliega la lista de tipos de items registrados en el sistema"""
	if request.method == "POST":
		formulario = TipoItemForm(request.POST, request.FILES)

		if formulario.is_valid():
			#forma para poder ingresar a los datos del formulario, tal vez para hacer nuestras propias validaciones
			print "==============================================="
			print formulario.cleaned_data['nombre']
			print "==============================================="
			formulario.save()
			return HttpResponseRedirect('/tipoItem')

	else:
		formulario=TipoItemForm()

	return render(request, 'tipoItem_form.html', {'formulario': formulario,})

@login_required(login_url='/ingresar')
def eliminarItem(request, codigo):
    """Funcion que elimina un tipo de atributo que no este asociado a ningun tipo de item. \nRecibe @param un request,
    peticion de operacion, y el codigo del tipo de atributo a eliminar. Elimina el mismo y\n @return a la interfaz
    donde se despliega la lista de tipos de atributos existentes en el sistema."""
    item= Item.objects.get(pk=codigo) # request.GET.get('codigo')
    return render_to_response('eliminarItem.html',{'item':item}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def eliItem(request, codigo):
    """Funcion que elimina un tipo de atributo que no este asociado a ningun tipo de item. \nRecibe @param un request,
    peticion de operacion, y el codigo del tipo de atributo a eliminar. Elimina el mismo y\n @return a la interfaz
    donde se despliega la lista de tipos de atributos existentes en el sistema."""
    item=Item.objects.get(pk=codigo)
    if request.method == "POST":
        formulario = EliminarItemForm(request.POST, request.FILES, instance = item)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/item')
    else:
        formulario=EliminarItemForm(instance = item)
    return render(request,'eliminarItem1.html', {'formulario': formulario})

        #item.estado= 'Desactivado'
        #return HttpResponseRedirect('/item')
@login_required(login_url='/ingresar')
def revivirItem(request, codigo):
    """Funcion que revive un item eliminado. \nRecibe @param un request,
    peticion de operacion, y el codigo del item a revivir. Revive el mismo y\n @return a la interfaz
    donde se despliega la lista de items existentes en el sistema."""
    item=Item.objects.get(pk=codigo)
    if request.method == "POST":
        formulario = EliminarItemForm(request.POST, request.FILES, instance = item)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/item')
    else:
        formulario=EliminarItemForm(instance = item)
    return render(request,'revivirItem.html', {'formulario': formulario})

@login_required(login_url='/ingresar')
def generarlb(request):
	"""Permite generar una linea base dentro del proyecto en el sistema. Recibe como :param request que
	es la peticion de la operacion.Retorna :return el formulario con los campos a completar, se acepta la operacion
	y vuelve a la interfaz donde se despliega la lista de tipos de items registrados en el sistema"""
	if request.method == "POST":
		formulario = lbForm(request.POST, request.FILES)

		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')

	else:
		formulario=lbForm()

	return render(request, 'lbForm.html', {'formulario': formulario,})
