from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from personas.models import Persona
from personas.api.serializers import PersonasSerializer
#filtro
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class PersonasViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PersonasSerializer
    queryset=Persona.objects.all()
    #filtro
    filter_backends=[DjangoFilterBackend,OrderingFilter]
    filterset_fields=['nombre']
    ordening_fields='__all__'
    