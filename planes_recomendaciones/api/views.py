from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from planes_recomendaciones.api.permissions import IsAdminOrReadOnly
from rest_framework.filters import SearchFilter
from planes_recomendaciones.api.serializers import RecomendacionesSerializer
from planes_recomendaciones.models import RecomendacionesModel


class RecomendacionesApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = RecomendacionesModel.objects.filter(is_delete=False)
    serializer_class = RecomendacionesSerializer
    filter_backends = [SearchFilter]
    search_fields = ['clasificacion']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Recomendación creada exitosamente."},
            status=status.HTTP_200_OK
        )

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Recomendación actualizada exitosamente."},
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete=True
        instance.save()
        return Response(
            {"message": "Recomendación eliminada exitosamente."},
            status=status.HTTP_200_OK
        )
