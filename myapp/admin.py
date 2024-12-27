from django.contrib import admin
from .models import Componente, Colaborador, Sede, Perfil_Usuario

# Register your models here.
admin.site.register(Componente)
admin.site.register(Colaborador)
admin.site.register(Sede)
admin.site.register(Perfil_Usuario)