from django.contrib import admin

# Register your models here.
from personas.models import Persona

@admin.register(Persona)

class PersonaAdmin(admin.ModelAdmin):
    list_display=['id','nombre','apellido','telefono','correo','tipo_persona']
    