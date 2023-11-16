from django.contrib import admin

# Register your models here.
from  factura_v_carteras.models import Factura_v_Cartera


@admin.register(Factura_v_Cartera)

class Factura_v_carteradmin(admin.ModelAdmin):
    list_display=['id','factura_venta','cartera']
    
