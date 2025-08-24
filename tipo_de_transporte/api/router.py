from rest_framework.routers import DefaultRouter
from tipo_de_transporte.api.views import TipoDeTransporteApiViewSet

router_tipo_de_transporte = DefaultRouter()

router_tipo_de_transporte.register(prefix='tipo-de-transporte', basename='tipo de transporte', viewset=TipoDeTransporteApiViewSet)