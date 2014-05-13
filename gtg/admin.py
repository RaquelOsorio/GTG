from django.contrib import admin

# Register your models here.

from django.contrib import admin
from gtg.models import Usuario
admin.site.register(Usuario)

from gtg.models import Rol
from django.contrib import admin
from gtg.models import Usuario
admin.site.register(Rol)

from gtg.models import RolUsuario
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from gtg.models import TipoAtributo
from gtg.models import Proyectos
class UserProfileInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(RolUsuario)
admin.site.register(TipoAtributo)
admin.site.register(Proyectos)

