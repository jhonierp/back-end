from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from pagos.models import Pago
from pagos.api.serializers import PagosSerializer


class PagosViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PagosSerializer
    queryset=Pago.objects.all()
