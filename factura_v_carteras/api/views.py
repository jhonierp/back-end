from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from factura_v_carteras.models import Factura_v_Cartera
from factura_v_carteras.api.serializers import Factura_v_CarterasSerializer


class Factura_v_CarterasViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=Factura_v_CarterasSerializer
    queryset=Factura_v_Cartera.objects.all()
