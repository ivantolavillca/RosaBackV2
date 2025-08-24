from rest_framework.routers import DefaultRouter
from consumo_frutas_verduras.api.views import ConsumoFrutasVerdurasApiViewSet

router_consumo_frutas_verduras = DefaultRouter()

router_consumo_frutas_verduras.register(prefix='consumo-frutas-verduras', basename='consumo de frutas y verduras', viewset=ConsumoFrutasVerdurasApiViewSet)