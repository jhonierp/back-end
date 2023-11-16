from rest_framework.routers import DefaultRouter
from pagos.api.views import PagosViewSet


route_pago=DefaultRouter()


route_pago.register(
    prefix='pago',basename='pagos',viewset=PagosViewSet
    
)
