from django.contrib import admin

# Register your models here.
from productos.models import Producto


@admin.register(Producto)

class ProductoAdmin(admin.ModelAdmin):
    list_display=['id','codigo','nombre','descripcion','categoria','imagen','precio','estado','fecha_vencimiento']
    
