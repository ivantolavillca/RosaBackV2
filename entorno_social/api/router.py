from rest_framework.routers import DefaultRouter
from entorno_social.api.views import EntornoSocialApiViewSet

router_entorno_social = DefaultRouter()

router_entorno_social.register(prefix='entorno-social', basename='entorno social', viewset=EntornoSocialApiViewSet)