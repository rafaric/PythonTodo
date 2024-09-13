from django.contrib import admin
from .models import *

# Register your models here.

class TareasAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descripcion", "fecha_creacion", "estado")
    
    class Meta:
        verbose_name = "Tarea"


#(clase que está en models.py, clase que está en admin.py)
admin.site.register(Tarea, TareasAdmin)