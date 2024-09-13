from django.contrib import admin
from .models import *

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "biografia")


#(clase que está en models.py, clase que está en admin.py)
admin.site.register(Autor, AutorAdmin)