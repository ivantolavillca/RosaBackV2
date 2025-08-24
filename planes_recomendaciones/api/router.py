from rest_framework.routers import DefaultRouter

from planes_recomendaciones.api.views import RecomendacionesApiViewSet

router_recomendaciones = DefaultRouter()

router_recomendaciones.register(prefix='recomendaciones', basename='recomendaciones', viewset=RecomendacionesApiViewSet)