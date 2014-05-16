
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
    return render_to_response('gestionLB.html',{'lb': linea , 'fa': fa}, context_instance=RequestContext(request))

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
def fase1(request, codigo):
    """permite acceder a la interfaz de opciones de administracion para fases donde se despliega la lista de fases
    de cierto proyecto seleccionado.\n Recibe como @param request que es la peticion de la operacion y el codigo
    del proyecto, con el cual se filtra todas las fases pertenecientes al mismo. \n@return la lista de fases"""

    fases=Fases1.objects.filter(proyectos=codigo)
    proyecto= Proyectos.objects.get(pk=codigo)
    return render_to_response('gestionFase1.html',{'fases': fases, 'proyecto':proyecto }, context_instance=RequestContext(request))

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
        Permite registrar una nueva fase dentro del proyecto en el sistema.\nRecibe como @param reuqest que es la peticion
	    de la operacion. \nRetorna @return el formulario con todos los campos para registrar una nueva fase. Al aceptar la
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
def tipoItem(request):
    """permite acceder a la interfaz  de tipo de Item, donde se despliega la lista de todos los tipos de items
    registrados en el sistema. \nRecibe un @param request, peticion de operacion y \n@return la lista"""
    tItem=TipoItem.objects.all()
    return render_to_response('gestionTipoItem.html',{'tItem':tItem},context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def registrarTipoItem(request):
	"""Permite registrar un nuevo tipo de item a partir de un tipo de atributo dentro del proyecto en el sistema. \nRecibe como @param request que
	es la peticion de la operacion.\nRetorna @return el formulario con los campos a completar, se acepta la operacion
	y vuelve a la interfaz donde se despliega la lista de tipos de items registrados en el sistema"""
	if request.method == "POST":
		formulario = TipoItemForm(request.POST, request.FILES)

		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/tipoItem')

	else:
		formulario=TipoItemForm()

	return render(request, 'tipoItem_form.html', {'formulario': formulario,})

############### Vista Item #####################################################
##############################################################################
@login_required(login_url='/ingresar')
@login_required(login_url='/ingresar')
def item(request):
    """permite acceder a la interfaz de Item, donde se despliega la lista de todos los items
    registrados en el sistema. Recibe un :param request, peticion de operacion y :return la lista"""
    indice=0
    items=Item.objects.all().order_by('nombre') #[:10]
    priori= Item.objects.all()
    for i in priori:
        for it in items:
            if(it.nombre==i.nombre ):
                it=i
    p=1
    return render_to_response('gestionItem.html',{'items':items,'p':p},context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def registrarItem(request,codigo):
    """Permite registrar un nuevo item a partir de un tipo de item dentro del proyecto en el sistema. Recibe como :param request que
    es la peticion de la operacion.Retorna :return el formulario con los campos a completar, se acepta la operacion
    y vuelve a la interfaz donde se despliega la lista de items registrados en el sistema"""
    fase= Fases1.objects.get(pk=codigo)
    item= Item(fase=fase)
    formulario = ItemForm(request.POST, instance=item)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/item')
    else:
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
    ultima_version=0
    priori=0
    for itm in it:
        if(itm.nombre==item.nombre and itm.version >= ultima_version):
            ultima_version=itm.version
        if(itm.nombre==item.nombre and itm.prioridad>= priori):
            priori=itm.prioridad
    itms=Item(antecesorHorizontal=item.antecesorHorizontal,sucesorHorizontal=item.sucesorHorizontal,sucesorVertical=item.sucesorVertical,
            antecesorVertical=item.antecesorVertical,tipoItem=item.tipoItem,fase=item.fase,version=item.version, nombre=item.nombre, estado=item.estado,
            prioridad=-1, descripcion=item.descripcion)

    itemR = Item( antecesorHorizontal=item.antecesorHorizontal,sucesorHorizontal=item.sucesorHorizontal,sucesorVertical=item.sucesorVertical,
            antecesorVertical=item.antecesorVertical,tipoItem=item.tipoItem,fase=item.fase,version=ultima_version+1, nombre=item.nombre, estado=item.estado,
            prioridad=priori+1, descripcion=item.descripcion)

    formulario = ItemReversionar(request.POST, instance=itemR)
    if formulario.is_valid():
        formulario.save()

        return render(request, 'item_form1.html', {'formulario': formulario})
    else:
        return render(request, 'item_form1.html', {'formulario': formulario})



def relacionarItem(request, codigo,codigop):
    """Permite visualizar la lista de posibles items para relacionar a otro preciamente
     seleccionado :param request, que es la peticion de la operacion y el codigo del item
    a relacionar. Retorna :return a la interfaz de confirmacion de la operacion, esto es,despliega el
     formulario con las opciones de relacionar con un antecesor o sucesor del listado de items de existenes en el sistema"""

    item=Item.objects.get(pk=codigo)
    proyecto=Proyectos.objects.get(pk=codigop)
    fases=Fases1.objects.filter(proyectos=proyecto)
    items=Item.objects.all()
    return render(request,'listaRelacion.html', {'item': item,'items':items,'proyectos':proyecto,'fases':fases})


def relacItem(request, codigo,codigop):
    """Permite registrar un nuevo item a partir de un tipo de item dentro del proyecto en el sistema. Recibe como :param request que
    es la peticion de la operacion.Retorna :return el formulario con los campos a completar, se acepta la operacion
    y vuelve a la interfaz donde se despliega la lista de items registrados en el sistema"""
    item=Item.objects.get(pk=codigo)
    itemRelacionado=Item.objects.get(pk=codigop)
    if (item.fase.id == itemRelacionado.fase.id):
        item.antecesorVertical=itemRelacionado
    else:
        item.antecesorHorizontal=itemRelacionado

    if request.method == "POST":
        formulario = EliminarItemForm(request.POST, request.FILES, instance = item)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/item')
    else:
        formulario=EliminarItemForm(instance = item)
    return render(request,'relacionarItems.html', {'formulario': formulario})







######Vista de la lista de items pertenecientes a la fase selecionada##########
 ################################################################################
def itemFase(request, codigo):
    """permite acceder a la interfaz de opciones de administracion para fases donde se despliega la lista de fases
    de cierto proyecto seleccionado. Recibe como :param request que es la peticion de la operacion y el codigo
    del proyecto, con el cual se filtra todas las fases pertenecientes al mismo. :return la lista de fases"""
    items=Item.objects.filter(fase=codigo)
    fase=Fases1.objects.get(pk=codigo)
    return render_to_response('gestionItem1.html',{'items': items, 'fase':fase }, context_instance=RequestContext(request))

def itemTipoItem(request, codigo):
    """permite acceder a la interfaz de opciones de administracion para tipos de items donde se despliega la lista de fases
    de cierto proyecto seleccionado. Recibe como \n@param request que es la peticion de la operacion y el codigo
    del item, con el cual se filtra todas los tipos de item pertenecientes al mismo. \n@return la lista de items"""
    itemTipo=Item.objects.filter(tipoItem=codigo)
    item= Item.objects.get(pk=codigo)
    return render_to_response('gestionTipoItem1.html',{'itemTipo': itemTipo, 'item':item }, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def registrarTipoItem(request):
    """Permite registrar un nuevo tipo de item a partir de un tipo de atributo dentro del proyecto en el sistema.|n Recibe como @param request que
    es la peticion de la operacion.\nRetorna @return el formulario con los campos a completar, se acepta la operacion
    y vuelve a la interfaz donde se despliega la lista de tipos de items registrados en el sistema"""
    formulario = TipoItemForm(request.POST, request.FILES)
    if formulario.is_valid():
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
    item.estado='DESAC'
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
    item.estado='REDAC'
    if request.method == "POST":
        formulario = EliminarItemForm(request.POST, request.FILES, instance = item)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/item')
    else:
        formulario=EliminarItemForm(instance = item)
    return render(request,'revivirItem.html', {'formulario': formulario})

####desde aqui modifique

TEMPL_RELACION_FORM = 'form_relacion.html'
TEMPL_RELACION_LISTA = 'lista_relaciones.html'


class CreaRelacionView(CreateView):

    """
    Vista que permite crear relaciones entre items.
    De una misma fase.
    De fases antecesoras.
    """

    model = ItemRelacion
    template_name = TEMPL_RELACION_FORM
    form_class = ItemRelacionForm
    valido = True


    #def get_success_url(self):
     #   return reverse('relacion_listar', codigo)

    def get_form(self, form_class):
        form = CreateView.get_form(self, form_class)
        #el selector solo debe desplegar los items del proyecto
        #fases = Fase.objects.filter(idproyecto_id=self.kwargs['idproyecto'])

        fases = Fases1.objects.filter(proyectos=self.kwargs['id'])
        #lista los items que coinciden con las fases de proyecto
        items = Item.objects.filter(fase=fases).exclude(estado=Item.E_DESACTIVADO)
        #cargamos los selectores con los items y mostrando a que fase pertenecen
        opciones = [(item.pk,'['+ item.fase.__str__()[0:5]+'..] ' +\
                     '[' + item.estado +']  | ' +
                      item.nombre[0:40] ) for item in items]
        form.fields['origen'].choices = opciones
        form.fields['destino'].choices = opciones
        return form
"""
    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context['action'] = reverse('relacion_crear',codigo)
        if not self.valido:
            context['nodefault'] = 'index2.html'

        return context

    def form_valid(self, form):
        #establece el tipo de la relacion , si es interna a la fase o externa
        # es decir padre e hijo o antecesor sucesor.
        form.instance.set_tipo()
        origen = form.instance.origen
        destino = form.instance.destino
        #Serie de validaciones
        if self.valid_relacion_unica(origen, destino):
            messages.error(self.request, 'La relacion ya existe: ' + \
                           origen.__str__()+ ' --> '+ destino.__str__())
            self.valido = False
            return self.form_invalid(form)

        if self.valid_existe_ciclo(form.instance.origen_id, form.instance.destino_id):
            messages.error(self.request, 'se ha detectado un ciclo: ' + \
                origen.__str__()+ ' --> '+ destino.__str__())

            self.valido = False
            return self.form_invalid(form)



        return CreateView.form_valid(self, form)

    def form_invalid(self, form):
        self.valido = False
        return CreateView.form_invalid(self, form)

    @classmethod
    def __lista_antecesores(self,idItem):
        #retorno = list(db.session.query(Relacion).filter(Relacion.idSucesor == idItem ).all())
        retorno = ItemRelacion.objects.filter(destino_id=idItem)
        antecesores = []
        for r in retorno:
            antecesores.append(r.origen_id)
            antecesores += self.__lista_antecesores(r.origen_id)
        return antecesores

    @classmethod
    def __lista_sucesores(self,idItem):
        #retorno = list(db.session.query(Relacion).filter(Relacion.idAntecesor == idItem ).all())
        retorno = ItemRelacion.objects.filter(origen_id=idItem)
        sucesores = []
        for r in retorno:
            sucesores.append(r.destino_id)
            sucesores += self.__lista_sucesores(r.destino_id)
        return sucesores

    @classmethod
    def valid_existe_ciclo(self, idorigen, iddestino):


        Destecta un ciclo en un par de items (origen , destino).

        Se carga listas todos los de origenes posibles y destinos posibles
        Se itera para verificar si existe alguna forma de llegar
        al origen por medio del destino
        Retorna True si existe el camino.


        # caso autociclo
        if idorigen == iddestino:
            return True
        a = self.__lista_antecesores(idorigen)
        b = self.__lista_sucesores(iddestino)
        # caso sencillo 1->2, 2->1
        for ante in a:
            if str(ante) == str(iddestino):
                return True
        #otros casos
        for isgte in a:
            for iant in b:
                if( isgte == iant):
                    return True

        return False

    @classmethod
    def valid_relacion_unica(self,porigen, pdestino):


        Valida que aun no exista la relacion.
        -Tiene en cuenta que pueden existir relaciones eliminadas y las ignora.


        relacion = ItemRelacion.objects.filter(Q(origen=porigen) & Q(destino=pdestino)).\
        exclude(estado=ItemRelacion.E_ELIMINADO)
        return relacion.count()

class ListaRelacionesView(ListView,codigo):


    Vista que consulta las relaciones a nivel de :
    -Fase.
    -Item.
    -Proyecto en general.

    model = ItemRelacion
    template_name = TEMPL_RELACION_LISTA

    def get_queryset(self):

        #lista las relaciones que tiene una fase
        if self.kwargs.get('fase',None):
            object_list = None

        #lista todas las relaciones que implican ese item
        if self.kwargs.get('nroItem',None):
            object_list = ItemRelacion.objects.filter().all()

        #lista todas las relaciones que implican ese item
        if self.kwargs.get(codigo,None):
            #No es optima esta consulta
            fases=Fases1.objects.filter(proyectos=codigo)

            #fases = Fases1.objects.filter(idproyecto_id=self.kwargs.get('idproyecto'))
            items = Item.objects.filter(fase=fases)

            object_list = ItemRelacion.objects.filter((Q(origen__in=items)|\
                                                       Q(destino__in=items)) &\
                                                    Q(estado=ItemRelacion.E_ACTIVO))
        return object_list

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context['proyecto'] = self.kwargs.get(codigo)
        return context
"""
@login_required(login_url='/ingresar')
def generarlb(request, codigo):
    """Permite generar una linea base dentro del proyecto en el sistema. Recibe como :param request que
    es la peticion de la operacion.Retorna :return el formulario con los campos a completar, se acepta la operacion
    y vuelve a la interfaz donde se despliega la lista de tipos de items registrados en el sistema"""
    fase= Fases1.objects.get(pk=codigo)
    lineaB= lineaBase(fase=fase)
    formulario = lbForm(request.POST, request.FILES, instance=lineaB)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/')
    else:
        formulario=lbForm(instance=lineaB)

	return render(request, 'lbForm.html', {'formulario': formulario,})

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
def relaionarItemLb(request, codigo, codigo1):
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
    faseI=Fases1(fechaInicio=fase.fechaInicio,fechaFin=fase.fechaFin,nombre=fase.nombre,descripcion=fase.descripcion,estado=fase.estado)
    formulario = importarFaseForm(request.POST, instance=faseI)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/fase')
    else:
        return render(request, 'faseImport.html', {'formulario': formulario})


