from rest_framework import serializers
from stock.models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields=['id','producto_stock','cantidad','lote_stock']