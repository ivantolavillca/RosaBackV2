from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from consumo_comida_rapida.api.permissions import IsAdminOrReadOnly
from rest_framework.filters import SearchFilter
from consumo_frutas_verduras.api.serializers import ConsumoFrutasVerdurasSerializer
from consumo_frutas_verduras.models import consumo_frutas_verduras


class ConsumoFrutasVerdurasApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = consumo_frutas_verduras.objects.filter(is_delete=False)
    serializer_class = ConsumoFrutasVerdurasSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Consumo de frutas y verduras creada exitosamente."},
            status=status.HTTP_200_OK
        )

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Consumo de frutas y verduras actualizada exitosamente."},
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete=True
        instance.save()
        return Response(
            {"message": "Consumo de frutas y verduras eliminada exitosamente."},
            status=status.HTTP_200_OK
        )
