from rest_framework import serializers
from carteras.models import Cartera

class CarterasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cartera
        fields=['id','fecha_facturacion','fecha_vencimiento','pago']