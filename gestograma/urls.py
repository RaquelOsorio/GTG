
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$','gtg.views.ingresar'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^administrar/$','gtg.views.administrar'),
    url(r'^privado/$','gtg.views.privado'),

)
#url(r'^ingresar/$','gtg.views.ingresar'),