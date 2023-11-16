from django.contrib import admin

# Register your models here.
from pagos.models import Pago

@admin.register(Pago)

class PagoAdmin(admin.ModelAdmin):
    list_display=['id','medio_pago','estado_pago','factura_v','factura_c']
    
