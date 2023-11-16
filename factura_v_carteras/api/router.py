from rest_framework.routers import DefaultRouter
from factura_v_carteras.api.views import Factura_v_CarterasViewSet


route_f_v_carteras=DefaultRouter()


route_f_v_carteras.register(
    prefix='factura_v_cartera',basename='factura_v_carteras',viewset=Factura_v_CarterasViewSet
    
)
