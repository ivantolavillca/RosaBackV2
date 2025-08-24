from rest_framework.routers import DefaultRouter
from horas_de_sueno.api.views import HorasDeSuenoApiViewSet

router_horas_de_sueno = DefaultRouter()

router_horas_de_sueno.register(prefix='horas-de-sueno', basename='horas de sueño', viewset=HorasDeSuenoApiViewSet)