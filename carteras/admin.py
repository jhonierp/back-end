from django.contrib import admin

# Register your models here.
from carteras.models import Cartera


@admin.register(Cartera)

class CarteraAdmin(admin.ModelAdmin):
    list_display=['id','fecha_facturacion','fecha_vencimiento','pago']
    
