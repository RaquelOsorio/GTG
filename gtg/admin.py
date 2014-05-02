from django.contrib import admin

# Register your models here.

<<<<<<< HEAD
from gtg.models import Roles
from django.contrib import admin
from gtg.models import Usuario
admin.site.register(Roles)
admin.site.register(Usuario)
from gtg.models import ModificarRol
from gtg.models import RolesUsuario
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
admin.site.register(RolesUsuario)
admin.site.register(ModificarRol)
admin.site.register(TipoAtributo)
admin.site.register(Proyectos)
=======
<<<<<<< HEAD
from gtg.models import Rol
from django.contrib import admin
from gtg.models import Proyecto
>>>>>>> 64570d5fc03175bcdd7814fba88c89225e9a231d

admin.site.register(Rol)
admin.site.register(Proyecto)
=======
#from gtg.models import AltaUser
from django.contrib import admin
>>>>>>> 422ad2cad28d48cc948a7890ed3910fb77c281e1
