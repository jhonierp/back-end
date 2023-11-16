from rest_framework import serializers
from factura_ventas.models import Factura_Venta

class FacturaVentasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Factura_Venta
        fields=['id','fecha_ingreso','cliente_f','total_v']