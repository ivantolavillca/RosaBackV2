from rest_framework.routers import DefaultRouter
from tiempo_en_pantallas.api.views import TiempoEnPantallasApiViewSet

router_tiempo_en_pantallas = DefaultRouter()

router_tiempo_en_pantallas.register(prefix='tiempo-en-pantallas', basename='tiempo en pantallas', viewset=TiempoEnPantallasApiViewSet)