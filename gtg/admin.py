from django.contrib import admin

# Register your models here.

from gtg.models import Rol
from django.contrib import admin
from gtg.models import Proyecto

admin.site.register(Rol)
admin.site.register(Proyecto)