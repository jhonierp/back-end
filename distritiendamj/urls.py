
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.api.router import route_user
from lotes.api.router import route_lote
from productos.api.router import route_producto
from categorias.api.router import route_categoria
from stock.api.router import route_stock
from factura_compras.api.router import route_fcompra
from personas.api.router import route_persona
from detalle_compras.api.router import route_dcompra
from factura_ventas.api.router import route_fventa
from detalle_ventas.api.router import route_dventa
from pagos.api.router import route_pago
from carteras.api.router import route_cartera
from factura_v_carteras.api.router import route_f_v_carteras

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="API distritiendamj",
      default_version='v1',
      description="Documentación Api distritiendamj",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="wilson.199819@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
from users.models import User

urlpatterns = [
   path('admin/', admin.site.urls),
   path('documentacionapi<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('documentacionapi/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('api',include('users.api.router')),
   path('api',include(route_user.urls)),
   path('api',include(route_lote.urls)),
   path('api',include(route_producto.urls)),
   path('api',include(route_categoria.urls)),
   path('api',include(route_stock.urls)),
   path('api',include(route_fcompra.urls)),
   path('api',include(route_persona.urls)),
   path('api',include(route_dcompra.urls)),
   path('api',include(route_fventa.urls)),
   path('api',include(route_dventa.urls)),
   path('api',include(route_pago.urls)),
   path('api',include(route_cartera.urls)),
   path('api',include(route_f_v_carteras.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
