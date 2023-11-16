from rest_framework import serializers
from factura_v_carteras.models import Factura_v_Cartera


class Factura_v_CarterasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Factura_v_Cartera
        fields=['id','factura_venta','cartera']