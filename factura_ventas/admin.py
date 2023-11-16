from django.contrib import admin

# Register your models here.
from factura_ventas.models import Factura_Venta


@admin.register(Factura_Venta)

class FacturaVentaAdmin(admin.ModelAdmin):
    list_display=['id','fecha_ingreso','cliente_f','total_v']
    
