from rest_framework.routers import DefaultRouter
from consumo_alcohol.api.views import ConsumoBebidasAlcoholicasApiViewSet

router_consumo_alcohol = DefaultRouter()

router_consumo_alcohol.register(prefix='consumo-bebidas-alcoholicas', basename='consumo bebidas alcoholicas', viewset=ConsumoBebidasAlcoholicasApiViewSet)