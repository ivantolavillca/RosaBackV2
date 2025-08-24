from rest_framework.routers import DefaultRouter
from habitos_alimentarios.api.views import HabitosAlimentariosApiViewSet

router_habitos_alimentarios = DefaultRouter()

router_habitos_alimentarios.register(prefix='habitos-alimentarios', basename='habitos alimentarios', viewset=HabitosAlimentariosApiViewSet)