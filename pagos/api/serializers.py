from rest_framework import serializers
from pagos.models import Pago


class PagosSerializer(serializers.ModelSerializer):
   # fcompra_data=FacturaVentasSerializer(source='factura_compra',read_only=True)
    class Meta:
        model=Pago
        fields=['id','medio_pago','estado_pago','factura_v','factura_c']