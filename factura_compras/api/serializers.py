from rest_framework import serializers
from factura_compras.models import Factura_Compra

class FacturaComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Factura_Compra
        fields=['id','fecha_ingreso','proveedor_f','total_c']