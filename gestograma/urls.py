
from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
from gtg import views
admin.autodiscover()

#from gtg.views import CreaRelacionView, ListaRelacionesView

urlpatterns = patterns('',

    url(r'^$','gtg.views.ingresar'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^administrar/(?P<codigoProyecto>\d+)/$','gtg.views.administrar'),
    url(r'^desarrollo/$','gtg.views.desarrollo'),
    url(r'^configuracion/$','gtg.views.configuracion'),
    url(r'^privado/$','gtg.views.privado'),
    url(r'^cerrar/$','gtg.views.cerrar'),
    url(r'^usuario/consultarUsuario/(?P<codigo>\d+)/$', 'gtg.views.consultarUsuario'),

    url(r'^usuario/$','gtg.views.usuario'),
    url(r'^comite/(?P<codigoProyecto>\d+)/$','gtg.views.comite'),
    url(r'^incluir_al_Comite/(?P<codigoProyecto>\d+)/$','gtg.views.incluir_al_Comite'),

    url(r'^proyecto/$','gtg.views.proyecto'),

    url(r'^usuario/$','gtg.views.usuario'),
    url(r'^proyecto/$','gtg.views.proyecto'),
    url(r'^proyectoAdmin/$','gtg.views.proyectoAdmin'),
    url(r'^proyecto/buscar/$','views.buscarProyecto'),

    url(r'^fase1/(?P<codigoProyecto>\d+)/$','gtg.views.fase1'),
    url(r'^fase1/registrarFase/(?P<codigo>\d+)/$','gtg.views.registrarFase'),
    #url(r'^fase/$','gtg.views.fase'),
    url(r'^fase1/$','gtg.views.fase1'),
    url(r'^rolPermiso/$','gtg.views.rolPermiso'),
    url(r'^tipoItem/(?P<codigoProyecto>\d+)/$','gtg.views.tipoItem'),
    url(r'^item/(?P<codigoProyecto>\d+)/$','gtg.views.item'),
    url(r'^lb/(?P<codigo>\d+)/$','gtg.views.lb'),
    url(r'^lb/generarlb/(?P<codigo>\d+)/$','gtg.views.generarlb'),
    url(r'^lb/cambioEstadoLb/(?P<codigo>\d+)/$','gtg.views.cambioEstadoLb'),
    url(r'^proyecto/importarProyecto/(?P<codigo>\d+)/$','gtg.views.importarProyecto'),
    url(r'^cambio/(?P<codigoProyecto>\d+)/$','gtg.views.cambio'),
    url(r'^usuario/nuevo_usuario/$','gtg.views.nuevo_usuario'),
    url(r'^usuario/nuevo_rolusuario/$','gtg.views.nuevo_rolusuario'),
    url(r'^rolPermiso/registrarRol/$','gtg.views.registrarRol'),
    url(r'^rolPermiso/lista_roles/$','gtg.views.lista_roles'),
    url(r'^rolPermiso/eliminar_rol/(?P<codigo>\d+)/$', 'gtg.views.eliminar_rol'),
    url(r'^eliRol/(?P<codigo>\d+)/$', 'gtg.views.eliRol'),

    url(r'^proyecto/registrarProyecto/$','gtg.views.registrarProyecto'),
   url(r'^fase/lista_proyecto/$','gtg.views.lista_proyectos'),
   #url(r'^fase/registrarFase/$','gtg.views.registrarFase'),
   url(r'^rolPermiso/lista_rolesModificar/$','gtg.views.lista_rolesModificar'),
   url(r'^rolPermiso/editar/(?P<codigo>\d+)/$', 'gtg.views.editar'),
   url(r'^usuario/lista_usuarios/$','gtg.views.lista_usuarios'),
   url(r'^usuario/editarUsuario/(?P<codigo>\d+)/$', 'gtg.views.editarUsuario'),
   # url(r'^fase/lista_Fase/$','gtg.views.lista_Fase'),
   # url(r'^fase/registrarFase/(?P<codigo>\d+)/$','gtg.views.registrarFase'),
    url(r'^fase/editarFase/(?P<codigo>\d+)/$', 'gtg.views.editarFase'),
    #url(r'^fase/lista_Faseeliminar/$','gtg.views.lista_Faseeliminar'),
    url(r'^fase/eliminar_fase/(?P<codigo>\d+)/$', 'gtg.views.eliminar_fase'),

    url(r'^proyecto/lista_ProyectoEditar/$','gtg.views.lista_ProyectoEditar'),
    url(r'^proyecto/editarProyecto/(?P<codigo>\d+)/$', 'gtg.views.editarProyecto'),
    url(r'^proyecto/verProyecto/(?P<codigo>\d+)/$', 'gtg.views.verProyecto'),

    url(r'^tipoAtributo/$','gtg.views.tipoAtributo'),
    url(r'^tipoAtributo/registrarTipoAtributo/$','gtg.views.registrarTipoAtributo'),
    url(r'^tipoAtributo/eliminar_tipoAtributo/(?P<codigo>\d+)/$', 'gtg.views.eliminar_tipoAtributo'),
    url(r'^tipoAtributo/modificar_tipoAtributo/(?P<codigo>\d+)/$', 'gtg.views.modificar_tipoAtributo'),

    url(r'^eliTipoAtributo/(?P<codigo>\d+)/$', 'gtg.views.eliTipoAtributo'),
    url(r'^tipoItem/registrarTipoItem/(?P<codigoProyecto>\d+)/$','gtg.views.registrarTipoItem'),
    url(r'^item/$','gtg.views.item'),
    url(r'^item/registrarItem/(?P<codigo>\d+)/$','gtg.views.registrarItem'),
    url(r'^item/modificarItem/(?P<codigo>\d+)/$', 'gtg.views.modificarItem'),
    url(r'^item/reversionarItem/(?P<codigo>\d+)/$', 'gtg.views.reversionarItem'),
   # url(r'^item/relacionarItem/(?P<codigo>\d+)/$', 'gtg.views.relacionarItem'),

    url(r'^item/relacionarItem/(?P<codigo>\d+)/(?P<codigop>\d+)/$', 'gtg.views.relacionarItem'),
    url(r'^item/relacItem/(?P<codigo>\d+)/(?P<codigop>\d+)/$', 'gtg.views.relacItem'),
    url(r'^itemFase/(?P<codigo>\d+)/$','gtg.views.itemFase'),
    url(r'^importarFase/(?P<codigo>\d+)/$','gtg.views.importarFase'),
    url(r'^finalizarFase/(?P<codigo>\d+)/$','gtg.views.finalizarFase'),
   # url(r'^fase1/$','gtg.views.fase'),
  #  url(r'^itemTipoItem/(?P<codigo>\d+)/$','gtg.views.itemTipoItem'),

   url(r'^usuario/consultarUsuario/(?P<codigo>\d+)/$', 'gtg.views.consultarUsuario'),
    #url(r'^fase/lista_Fase/$','gtg.views.lista_Fase'),
   # url(r'^fase/lista_Fase/$','gtg.views.lista_Fase'),
   # url(r'^fase/registrarFase/(?P<codigo>\d+)/$','gtg.views.registrarFase'),
    url(r'^fase/editarFase/(?P<codigo>\d+)/$', 'gtg.views.editarFase'),
    #url(r'^fase/lista_Faseeliminar/$','gtg.views.lista_Faseeliminar'),
    url(r'^fase/eliminar_fase/(?P<codigo>\d+)/$', 'gtg.views.eliminar_fase'),
    url(r'^eliFase/(?P<codigo>\d+)/$', 'gtg.views.eliFase'),

    url(r'^proyecto/lista_ProyectoEditar/$','gtg.views.lista_ProyectoEditar'),
    url(r'^proyecto/editarProyecto/(?P<codigo>\d+)/$', 'gtg.views.editarProyecto'),
    url(r'^tipoAtributo/$','gtg.views.tipoAtributo'),
    url(r'^tipoAtributo/registrarTipoAtributo/$','gtg.views.registrarTipoAtributo'),
    url(r'^tipoAtributo/eliminar_tipoAtributo/(?P<codigo>\d+)/$', 'gtg.views.eliminar_tipoAtributo'),
    url(r'^tipoAtributo/modificar_tipoAtributo/(?P<codigo>\d+)/$', 'gtg.views.modificar_tipoAtributo'),

    url(r'^eliTipoAtributo/(?P<codigo>\d+)/$', 'gtg.views.eliTipoAtributo'),
   # url(r'^tipoItem/registrarTipoItem/$','gtg.views.registrarTipoItem'),
    url(r'^item/eliminarItem/(?P<codigo>\d+)/$', 'gtg.views.eliminarItem'),
    url(r'^eliItem/(?P<codigo>\d+)/$', 'gtg.views.eliItem'),
    url(r'^item/revivirItem/(?P<codigo>\d+)/$', 'gtg.views.revivirItem'),
    url(r'^lb/listaItemsTer/(?P<codigo>\d+)/$', 'gtg.views.listaItemsTer'),
    url(r'^listaItemsTer/relaionarItemLb/(?P<codigo>\d+)/(?P<codigo1>\d+)/$', 'gtg.views.relacionarItemLb'),
    #url(r'^comite/(?P<codigoProyecto>\d+)/$','gtg.views.comite'),
    url(r'^incluir_al_Comite/(?P<codigoProyecto>\d+)/(?P<codigoUsuario>\d+)/$','gtg.views.incluir_al_Comite'),
    url(r'^listaSolicitudes/$', 'gtg.views.listaSolicitudes'),
    url(r'^itemFase/crearSolicitudCambio/(?P<codigo>\d+)/$', 'gtg.views.crearSolicitudCambio'),
    url(r'^listaSolicitudes/consultarSolicitud/(?P<id_solicitud>\d+)/$', 'gtg.views.consultarSolicitud'),
    url(r'^listaSolicitudes/votar/(?P<codigo>\d+)/$', 'gtg.views.votar'),
    url(r'^voto/$', 'gtg.views.voto'),
    url(r'^listaLbRota/$', 'gtg.views.listaLbRota'),
    url(r'^listalbRota/listaItemLbRota/(?P<codigo>\d+)/$', 'gtg.views.listaItemRev'),
    url(r'^listalbRota/historialCambio/(?P<codigo>\d+)/$', 'gtg.views.historialCambio'),
     url(r'^modificarItemVal/(?P<codigo>\d+)/$', 'gtg.views.modificarItemVal'),
    url(r'^consultarItem/(?P<codigo>\d+)/$', 'gtg.views.consultarItem'),
    url(r'^listaItemsProyecto/(?P<codigo>\d+)/$', 'gtg.views.listaItemsProyecto'),
    url(r'^listaItemsProyecto/calcularImpacto/(?P<codigo>\d+)/$', 'gtg.views.calcularImpacto'),

    url(r'^reporte/usuario/$','gtg.views.descargar_reporteUsuarios'),
    url(r'^reporte/rol/$','gtg.views.descargar_reporteRoles'),

    url(r'^reporte/proyecto/$','gtg.views.descargar_reporteProyectos'),
    url(r'^reporte/proyecto/lineasBase/(?P<codigo>\d+)$','gtg.views.descargar_reporteLB'),
    url(r'^reporte/proyecto/solicitudesCambio/(?P<codigo>\d+)$','gtg.views.descargar_reporteSolicitudes'),
    url(r'^reporte/proyecto/items/(?P<codigo>\d+)$','gtg.views.descargar_reporteItems'),
    url(r'^finalizarProyecto/(?P<codigo>\d+)/$','gtg.views.finalizarProyecto'),




#relaciones
   # url(r'^relacion/crear/(?P<idproyecto>\d+)$', CreaRelacionView.as_view(), name="relacion_crear"),
    #url(r'^relaciones/listar/(?P<idproyecto>\d+)$', ListaRelacionesView.as_view(), name="relacion_listar"),

    )
