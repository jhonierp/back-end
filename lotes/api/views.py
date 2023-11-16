from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from lotes.models import Lote
from lotes.api.serializers import LotesSerializer
#filtro
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class LotesViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=LotesSerializer
    queryset=Lote.objects.all()
    #filtro
    filter_backends=[DjangoFilterBackend,OrderingFilter]
    filterset_fields=['producto_lote']
    ordening_fields='__all__'
    