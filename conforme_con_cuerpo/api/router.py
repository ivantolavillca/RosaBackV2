from rest_framework.routers import DefaultRouter

from conforme_con_cuerpo.api.views import ConformeConCuerpoApiViewSet

router_conforme_de_cuerpo = DefaultRouter()

router_conforme_de_cuerpo.register(prefix='conforme-de-cuerpo', basename='conforme de cuerpo', viewset=ConformeConCuerpoApiViewSet)