from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from stock.models import Stock
from stock.api.serializers import StockSerializer
#filtro
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class StockViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=StockSerializer
    queryset=Stock.objects.all()
    #filtro
    filter_backends=[DjangoFilterBackend,OrderingFilter]
    filterset_fields=['cantidad']
    ordening_fields='__all__'
    