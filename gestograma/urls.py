
from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$','gtg.views.ingresar'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^administrar/$','gtg.views.administrar'),
    url(r'^desarrollo/$','gtg.views.desarrollo'),
    url(r'^configuracion/$','gtg.views.configuracion'),
    url(r'^privado/$','gtg.views.privado'),
<<<<<<< HEAD
    url(r'^cerrar/$','gtg.views.cerrar'),
    url(r'^usuario/consultarUsuario/(?P<codigo>\d+)/$', 'gtg.views.consultarUsuario'),

=======
    url(r'^tipoAtributo/$','gtg.views.tipoAtributo'),
>>>>>>> 64570d5fc03175bcdd7814fba88c89225e9a231d
    url(r'^usuario/$','gtg.views.usuario'),
    url(r'^proyecto/$','gtg.views.proyecto'),
    url(r'^fase1/(?P<codigo>\d+)/$','gtg.views.fase1'),
    url(r'^fase1/registrarFase/$','gtg.views.registrarFase'),
    url(r'^fase/$','gtg.views.fase'),

    url(r'^rolPermiso/$','gtg.views.rolPermiso'),
    url(r'^tipoItem/$','gtg.views.tipoItem'),
    url(r'^item/$','gtg.views.item'),
    url(r'^lb/$','gtg.views.lb'),
    url(r'^cambio/$','gtg.views.cambio'),
<<<<<<< HEAD
    url(r'^usuario/nuevo_usuario/$','gtg.views.nuevo_usuario'),
    url(r'^usuario/nuevo_rolusuario/$','gtg.views.nuevo_rolusuario'),
    url(r'^rolPermiso/registrarRol/$','gtg.views.registrarRol'),
    url(r'^rolPermiso/lista_roles/$','gtg.views.lista_roles'),
    url(r'^rolPermiso/eliminar_rol/(?P<codigo>\d+)/$', 'gtg.views.eliminar_rol'),
    url(r'^proyecto/registrarProyecto/$','gtg.views.registrarProyecto'),
   url(r'^fase/lista_proyecto/$','gtg.views.lista_proyectos'),
   url(r'^fase/registrarFase/$','gtg.views.registrarFase'),
   url(r'^rolPermiso/lista_rolesModificar/$','gtg.views.lista_rolesModificar'),
   url(r'^rolPermiso/editar/(?P<codigo>\d+)/$', 'gtg.views.editar'),
   url(r'^usuario/lista_usuarios/$','gtg.views.lista_usuarios'),
   url(r'^usuario/editarUsuario/(?P<codigo>\d+)/$', 'gtg.views.editarUsuario'),
    url(r'^fase/lista_Fase/$','gtg.views.lista_Fase'),
   # url(r'^fase/registrarFase/(?P<codigo>\d+)/$','gtg.views.registrarFase'),
    url(r'^fase/editarFase/(?P<codigo>\d+)/$', 'gtg.views.editarFase'),
    url(r'^fase/lista_Faseeliminar/$','gtg.views.lista_Faseeliminar'),
    url(r'^fase/eliminar_fase/(?P<codigo>\d+)/$', 'gtg.views.eliminar_fase'),

    url(r'^proyecto/lista_ProyectoEditar/$','gtg.views.lista_ProyectoEditar'),
    url(r'^proyecto/editarProyecto/(?P<codigo>\d+)/$', 'gtg.views.editarProyecto'),
    url(r'^proyecto/verProyecto/(?P<codigo>\d+)/$', 'gtg.views.verProyecto'),

    url(r'^tipoAtributo/$','gtg.views.tipoAtributo'),
    url(r'^tipoAtributo/registrarTipoAtributo/$','gtg.views.registrarTipoAtributo'),
    url(r'^tipoAtributo/eliminar_tipoAtributo/(?P<codigo>\d+)/$', 'gtg.views.eliminar_tipoAtributo'),
    url(r'^tipoAtributo/modificar_tipoAtributo/(?P<codigo>\d+)/$', 'gtg.views.modificar_tipoAtributo'),

    url(r'^eliTipoAtributo/(?P<codigo>\d+)/$', 'gtg.views.eliTipoAtributo'),
    url(r'^tipoItem/registrarTipoItem/$','gtg.views.registrarTipoItem'),
    url(r'^item/$','gtg.views.item'),
    url(r'^item/registrarItem/$','gtg.views.registrarItem'),
    url(r'^item/modificarItem/(?P<codigo>\d+)/$', 'gtg.views.modificarItem'),
    url(r'^itemFase/(?P<codigo>\d+)/$','gtg.views.itemFase'),
    url(r'^fase1/$','gtg.views.fase'),
    url(r'^itemTipoItem/(?P<codigo>\d+)/$','gtg.views.itemTipoItem'),




    )
=======
<<<<<<< HEAD
    url(r'^rolPermiso/registrarRol/$','gtg.views.registrarRol'),
    url(r'^rolPermiso/lista_roles/$','gtg.views.lista_roles'),
    url(r'^rolPermiso/lista_roles/eliminar_rol/$', 'gtg.views.eliminar_rol'),
    url(r'^proyecto/registrarProyecto/$','gtg.views.registrarProyecto'),



    #url(r'^roles/', include('gtg.urls', namespace="uroles")),
    #url(r'^list/$', 'gtg.views.RolList', name='plist'),
    #url(r'^add/$', 'gtg.views.add_Rol', name='padd'),


    )
#url(r'^ingresar/$','gtg.views.ingresar'),z
=======

    url(r'^cerrar/$','gtg.views.cerrar'),
    url(r'^proyecto/$','gtg.views.proyecto'),
    url(r'^rolesPermisos/$','gtg.views.rolesPermisos'),
    url(r'^tipoItem/$','gtg.views.tipoItem'),
    url(r'^solicitudCambio/$','gtg.views.solicitudCambio'),
    url(r'^usuario/nuevo/$','gtg.views.altaUsuario'),



)
#url(r'^ingresar/$','gtg.views.ingresar'),
>>>>>>> 422ad2cad28d48cc948a7890ed3910fb77c281e1
>>>>>>> 64570d5fc03175bcdd7814fba88c89225e9a231d
