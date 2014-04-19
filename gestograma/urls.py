
from django.conf.urls import patterns, include, url
from django.conf import settings
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
    url(r'^tipoAtributo/$','gtg.views.tipoAtributo'),
    url(r'^usuario/$','gtg.views.usuario'),
    url(r'^proyecto/$','gtg.views.proyecto'),
    url(r'^fase/$','gtg.views.fase'),
    url(r'^rolPermiso/$','gtg.views.rolPermiso'),
    url(r'^tipoItem/$','gtg.views.tipoItem'),
    url(r'^item/$','gtg.views.item'),
    url(r'^lb/$','gtg.views.lb'),
    url(r'^cambio/$','gtg.views.cambio'),

    url(r'^cerrar/$','gtg.views.cerrar'),
    url(r'^proyecto/$','gtg.views.proyecto'),
    url(r'^rolesPermisos/$','gtg.views.rolesPermisos'),
    url(r'^tipoItem/$','gtg.views.tipoItem'),
    url(r'^solicitudCambio/$','gtg.views.solicitudCambio'),
    url(r'^usuario/nuevo/$','gtg.views.altaUsuario'),



)
#url(r'^ingresar/$','gtg.views.ingresar'),
