from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from tipo_de_transporte.api.permissions import IsAdminOrReadOnly
from rest_framework.filters import SearchFilter
from tipo_de_transporte.api.serializers import CTipoDeTransporteSerializer
from tipo_de_transporte.models import tipo_de_transporte


class TipoDeTransporteApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = tipo_de_transporte.objects.filter(is_delete=False)
    serializer_class = CTipoDeTransporteSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Comida diaria creada exitosamente."},
            status=status.HTTP_200_OK
        )

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Comida diaria actualizada exitosamente."},
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete=True
        instance.save()
        return Response(
            {"message": "Comida diaria eliminada exitosamente."},
            status=status.HTTP_200_OK
        )
