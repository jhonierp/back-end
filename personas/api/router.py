from rest_framework.routers import DefaultRouter
from personas.api.views import PersonasViewSet


route_persona=DefaultRouter()


route_persona.register(
    prefix='personas',basename='personas',viewset=PersonasViewSet
    
)
