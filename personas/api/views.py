from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from personas.api.permissions import IsAdminOrReadOnly
from personas.api.serializers import PersonaSerializer, ReportPersonaSerializer,ModeloDatos
from rest_framework.pagination import LimitOffsetPagination
import os
from django.conf import settings
import tensorflow as tf
import joblib
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.utils import to_categorical
from personas.models import Personas
from sklearn.preprocessing import LabelEncoder
from rest_framework.test import APITestCase

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
model_path = os.path.join(settings.BASE_DIR, 'personas', 'obesidad_model.keras')
scaler_path = os.path.join(settings.BASE_DIR, 'personas', 'scaler.pkl')
label_encoder_path = os.path.join(settings.BASE_DIR, 'personas', 'label_encoder.pkl')
model = tf.keras.models.load_model(model_path)
scaler = joblib.load(scaler_path)
label_encoder = joblib.load(label_encoder_path)

class PredecirObesidadView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request):
        serializer = ModeloDatos(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        datos = serializer.validated_data
        imc = datos['peso'] / (datos['estatura'] ** 2)
        columnas = [
            'edad', 'peso', 'estatura', 'imc', 'genero', 'comida_diaria',
            'consumo_comida_rapida', 'consumo_frutas_verduras', 'consumo_alcohol',
            'horas_de_sueno', 'estres_ansiedad', 'conforme_con_cuerpo',
            'actividades_fisicas', 'tipo_de_transporte', 'tiempo_en_pantallas',
            'habitos_alimentarios', 'antecedentes_familiares', 'entorno_social',
            'condiciones_medicas', 'consumo_medicamentos', 'perimetro_cintura',
            'perimetro_cadera'
        ]
        datos_entrada = pd.DataFrame([[
            datos['edad'],
            datos['peso'],
            datos['estatura'],
            imc,
            datos['genero'],
            datos['comida_diaria'],
            int(datos['consumo_comida_rapida']),
            int(datos['consumo_frutas_verduras']),
            int(datos['consumo_alcohol']),
            datos['horas_de_sueno'],
            int(datos['estres_ansiedad']),
            int(datos['conforme_con_cuerpo']),
            int(datos['actividades_fisicas']),
            datos['tipo_de_transporte'],
            datos['tiempo_en_pantallas'],
            datos['habitos_alimentarios'],
            int(datos['antecedentes_familiares']),
            int(datos['entorno_social']),
            int(datos['condiciones_medicas']),
            int(datos['consumo_medicamentos']),
            datos['perimetro_cintura'],
            datos['perimetro_cadera']

        ]], columns=columnas)

        datos_entrada = scaler.transform(datos_entrada)
        try:
            prediccion = model.predict(datos_entrada)
            prediccion_clase = np.argmax(prediccion, axis=1)
            resultado = int(prediccion_clase[0])
            clasificacion = label_encoder.inverse_transform([resultado])[0]
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'prediccion': clasificacion}, status=status.HTTP_200_OK)


class PredecirObesidadApkView(APIView):
    #permission_classes = [IsAdminOrReadOnly]
    def post(self, request):
        serializer = ModeloDatos(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        datos = serializer.validated_data
        imc = datos['peso'] / (datos['estatura'] ** 2)
        columnas = [
            'edad', 'peso', 'estatura', 'imc','genero', 'comida_diaria',
            'consumo_comida_rapida', 'consumo_frutas_verduras', 'consumo_alcohol',
            'horas_de_sueno', 'estres_ansiedad', 'conforme_con_cuerpo',
            'actividades_fisicas', 'tipo_de_transporte', 'tiempo_en_pantallas',
            'habitos_alimentarios', 'antecedentes_familiares', 'entorno_social',
            'condiciones_medicas', 'consumo_medicamentos', 'perimetro_cintura',
            'perimetro_cadera'
        ]
        datos_entrada = pd.DataFrame([[
            datos['edad'],
            datos['peso'],
            datos['estatura'],
            imc,
            datos['genero'],
            datos['comida_diaria'],
            int(datos['consumo_comida_rapida']),
            int(datos['consumo_frutas_verduras']),
            int(datos['consumo_alcohol']),
            datos['horas_de_sueno'],
            int(datos['estres_ansiedad']),
            int(datos['conforme_con_cuerpo']),
            int(datos['actividades_fisicas']),
            datos['tipo_de_transporte'],
            datos['tiempo_en_pantallas'],
            datos['habitos_alimentarios'],
            int(datos['antecedentes_familiares']),
            int(datos['entorno_social']),
            int(datos['condiciones_medicas']),
            int(datos['consumo_medicamentos']),
            datos['perimetro_cintura'],
            datos['perimetro_cadera']

        ]], columns=columnas)

        datos_entrada = scaler.transform(datos_entrada)
        try:
            prediccion = model.predict(datos_entrada)
            prediccion_clase = np.argmax(prediccion, axis=1)
            resultado = int(prediccion_clase[0])
            clasificacion = label_encoder.inverse_transform([resultado])[0]
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'prediccion': clasificacion}, status=status.HTTP_200_OK)


class EntrenarYPredecirApkView(APIView):
    #permission_classes = [IsAdminOrReadOnly]
    def post(self, request):
        # Extraer datos de la base de datos
        queryset = Personas.objects.filter(is_delete=False).values( 'edad', 'peso', 'estatura', 'imc', 'genero', 'comida_diaria',
            'consumo_comida_rapida', 'consumo_frutas_verduras',
            'consumo_alcohol', 'horas_de_sueno', 'estres_ansiedad', 'conforme_con_cuerpo',
            'actividades_fisicas', 'tipo_de_transporte', 'tiempo_en_pantallas',
            'habitos_alimentarios', 'antecedentes_familiares', 'entorno_social',
            'condiciones_medicas', 'consumo_medicamentos', 'clasificacion','perimetro_cintura', 'perimetro_cadera')
        data = pd.DataFrame(queryset)

        # Validar que haya datos suficientes
        if data.empty or len(data) < 10:
            return Response({'error': 'No hay suficientes datos para entrenar el modelo.'},
                            status=status.HTTP_400_BAD_REQUEST)
        # data['genero'] = data['genero'].map({'Masculino': 1, 'Femenino': 0})
        # Preprocesar los datos
        data = data.dropna()  # Eliminar filas con valores nulos
        # data['imc'] = data['peso'] / (data['estatura'] ** 2)  # Calcular el IMC
        label_encoder = LabelEncoder()
        data['clasificacion'] = label_encoder.fit_transform(data['clasificacion'])  # Codificar la variable objetivo

        # Separar características y variable objetivo
        X = data[['edad', 'peso', 'estatura', 'imc', 'genero', 'comida_diaria',
                  'consumo_comida_rapida', 'consumo_frutas_verduras', 'consumo_alcohol',
                  'horas_de_sueno', 'estres_ansiedad', 'conforme_con_cuerpo',
                  'actividades_fisicas', 'tipo_de_transporte', 'tiempo_en_pantallas',
                  'habitos_alimentarios', 'antecedentes_familiares', 'entorno_social',
                  'condiciones_medicas', 'consumo_medicamentos', 'perimetro_cintura', 'perimetro_cadera']]
        y = data['clasificacion']
        y = to_categorical(y)  # Convertir las etiquetas a one-hot encoding

        # Dividir los datos en conjuntos de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Escalar las características
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Construir el modelo de red neuronal
        model = Sequential()
        model.add(Input(shape=(X_train.shape[1],)))  # Capa de entrada
        model.add(Dense(64, activation='relu'))  # Capa oculta 1
        model.add(Dense(32, activation='relu'))  # Capa oculta 2
        model.add(Dense(y.shape[1], activation='softmax'))  # Capa de salida

        # Compilar el modelo
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Entrenar el modelo
        model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

        # Realizar predicción con los datos enviados en la solicitud
        entrada = request.data
        try:

            edad = entrada['edad']
            peso = entrada['peso']
            estatura = entrada['estatura']
            imc = peso / (estatura ** 2)
            genero = entrada['genero']
            comida_diaria = entrada['comida_diaria']
            consumo_comida_rapida = int(entrada['consumo_comida_rapida'])
            consumo_frutas_verduras = int(entrada['consumo_frutas_verduras'])
            consumo_alcohol = int(entrada['consumo_alcohol'])
            horas_de_sueno = entrada['horas_de_sueno']
            estres_ansiedad = int(entrada['estres_ansiedad'])
            conforme_con_cuerpo = int(entrada['conforme_con_cuerpo'])
            actividades_fisicas = int(entrada['actividades_fisicas'])
            tipo_de_transporte = entrada['tipo_de_transporte']
            tiempo_en_pantallas = entrada['tiempo_en_pantallas']
            habitos_alimentarios = entrada['habitos_alimentarios']
            antecedentes_familiares = int(entrada['antecedentes_familiares'])
            entorno_social = int(entrada['entorno_social'])
            condiciones_medicas = int(entrada['condiciones_medicas'])
            consumo_medicamentos = int(entrada['consumo_medicamentos'])
            perimetro_cintura = entrada['perimetro_cintura']
            perimetro_cadera = entrada['perimetro_cadera']

            datos_entrada = pd.DataFrame([[
                edad,
                peso,
                estatura,
                imc,
                genero,
                comida_diaria,
                consumo_comida_rapida,
                consumo_frutas_verduras,
                consumo_alcohol,
                horas_de_sueno,
                estres_ansiedad,
                conforme_con_cuerpo,
                actividades_fisicas,
                tipo_de_transporte,
                tiempo_en_pantallas,
                habitos_alimentarios,
                antecedentes_familiares,
                entorno_social,
                condiciones_medicas,
                consumo_medicamentos,
                perimetro_cintura,
                perimetro_cadera
            ]], columns=[
                'edad', 'peso', 'estatura', 'imc', 'genero', 'comida_diaria',
                'consumo_comida_rapida', 'consumo_frutas_verduras', 'consumo_alcohol',
                'horas_de_sueno', 'estres_ansiedad', 'conforme_con_cuerpo',
                'actividades_fisicas', 'tipo_de_transporte', 'tiempo_en_pantallas',
                'habitos_alimentarios', 'antecedentes_familiares', 'entorno_social',
                'condiciones_medicas', 'consumo_medicamentos', 'perimetro_cintura',
                'perimetro_cadera'
            ])
            datos_entrada = scaler.transform(datos_entrada)
            prediccion = model.predict(datos_entrada)
            prediccion_clase = np.argmax(prediccion, axis=1)
            resultado = int(prediccion_clase[0])
            clasificacion = label_encoder.inverse_transform([resultado])[0]
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'prediccion': clasificacion}, status=status.HTTP_200_OK)


class EntrenarYPredecirView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request):
        # Extraer datos de la base de datos
        queryset = Personas.objects.filter(is_delete=False).values('edad', 'peso', 'estatura', 'imc', 'genero',
                                                                   'comida_diaria',
                                                                   'consumo_comida_rapida', 'consumo_frutas_verduras',
                                                                   'consumo_alcohol', 'horas_de_sueno',
                                                                   'estres_ansiedad', 'conforme_con_cuerpo',
                                                                   'actividades_fisicas', 'tipo_de_transporte',
                                                                   'tiempo_en_pantallas',
                                                                   'habitos_alimentarios', 'antecedentes_familiares',
                                                                   'entorno_social',
                                                                   'condiciones_medicas', 'consumo_medicamentos',
                                                                   'clasificacion', 'perimetro_cintura',
                                                                   'perimetro_cadera')
        data = pd.DataFrame(queryset)

        # Validar que haya datos suficientes
        if data.empty or len(data) < 10:
            return Response({'error': 'No hay suficientes datos para entrenar el modelo.'},
                            status=status.HTTP_400_BAD_REQUEST)
        # data['genero'] = data['genero'].map({'Masculino': 1, 'Femenino': 0})
        # Preprocesar los datos
        data = data.dropna()  # Eliminar filas con valores nulos
        # data['imc'] = data['peso'] / (data['estatura'] ** 2)  # Calcular el IMC
        label_encoder = LabelEncoder()
        data['clasificacion'] = label_encoder.fit_transform(data['clasificacion'])  # Codificar la variable objetivo

        # Separar características y variable objetivo
        X = data[['edad', 'peso', 'estatura', 'imc', 'genero', 'comida_diaria',
                  'consumo_comida_rapida', 'consumo_frutas_verduras', 'consumo_alcohol',
                  'horas_de_sueno', 'estres_ansiedad', 'conforme_con_cuerpo',
                  'actividades_fisicas', 'tipo_de_transporte', 'tiempo_en_pantallas',
                  'habitos_alimentarios', 'antecedentes_familiares', 'entorno_social',
                  'condiciones_medicas', 'consumo_medicamentos', 'perimetro_cintura', 'perimetro_cadera']]
        y = data['clasificacion']
        y = to_categorical(y)  # Convertir las etiquetas a one-hot encoding

        # Dividir los datos en conjuntos de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Escalar las características
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Construir el modelo de red neuronal
        model = Sequential()
        model.add(Input(shape=(X_train.shape[1],)))  # Capa de entrada
        model.add(Dense(64, activation='relu'))  # Capa oculta 1
        model.add(Dense(32, activation='relu'))  # Capa oculta 2
        model.add(Dense(y.shape[1], activation='softmax'))  # Capa de salida

        # Compilar el modelo
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Entrenar el modelo
        model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

        # Realizar predicción con los datos enviados en la solicitud
        entrada = request.data
        try:

            edad = entrada['edad']
            peso = entrada['peso']
            estatura = entrada['estatura']
            imc = peso / (estatura ** 2)
            genero = entrada['genero']
            comida_diaria = entrada['comida_diaria']
            consumo_comida_rapida = int(entrada['consumo_comida_rapida'])
            consumo_frutas_verduras = int(entrada['consumo_frutas_verduras'])
            consumo_alcohol = int(entrada['consumo_alcohol'])
            horas_de_sueno = entrada['horas_de_sueno']
            estres_ansiedad = int(entrada['estres_ansiedad'])
            conforme_con_cuerpo = int(entrada['conforme_con_cuerpo'])
            actividades_fisicas = int(entrada['actividades_fisicas'])
            tipo_de_transporte = entrada['tipo_de_transporte']
            tiempo_en_pantallas = entrada['tiempo_en_pantallas']
            habitos_alimentarios = entrada['habitos_alimentarios']
            antecedentes_familiares = int(entrada['antecedentes_familiares'])
            entorno_social = int(entrada['entorno_social'])
            condiciones_medicas = int(entrada['condiciones_medicas'])
            consumo_medicamentos = int(entrada['consumo_medicamentos'])
            perimetro_cintura = entrada['perimetro_cintura']
            perimetro_cadera = entrada['perimetro_cadera']

            datos_entrada = pd.DataFrame([[
                edad,
                peso,
                estatura,
                imc,
                genero,
                comida_diaria,
                consumo_comida_rapida,
                consumo_frutas_verduras,
                consumo_alcohol,
                horas_de_sueno,
                estres_ansiedad,
                conforme_con_cuerpo,
                actividades_fisicas,
                tipo_de_transporte,
                tiempo_en_pantallas,
                habitos_alimentarios,
                antecedentes_familiares,
                entorno_social,
                condiciones_medicas,
                consumo_medicamentos,
                perimetro_cintura,
                perimetro_cadera
            ]], columns=[
                'edad', 'peso', 'estatura', 'imc', 'genero', 'comida_diaria',
                'consumo_comida_rapida', 'consumo_frutas_verduras', 'consumo_alcohol',
                'horas_de_sueno', 'estres_ansiedad', 'conforme_con_cuerpo',
                'actividades_fisicas', 'tipo_de_transporte', 'tiempo_en_pantallas',
                'habitos_alimentarios', 'antecedentes_familiares', 'entorno_social',
                'condiciones_medicas', 'consumo_medicamentos', 'perimetro_cintura',
                'perimetro_cadera'
            ])
            datos_entrada = scaler.transform(datos_entrada)
            prediccion = model.predict(datos_entrada)
            prediccion_clase = np.argmax(prediccion, axis=1)
            resultado = int(prediccion_clase[0])
            clasificacion = label_encoder.inverse_transform([resultado])[0]
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'prediccion': clasificacion}, status=status.HTTP_200_OK)


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100
class PersonaApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Personas.objects.filter(is_delete=False).order_by('-id')
    serializer_class = PersonaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre_completo', 'edad', 'peso', 'estatura']
    pagination_class = CustomLimitOffsetPagination
    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Persona eliminada exitosamente."},
            status=status.HTTP_200_OK
        )
class ExportDataView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, format=None):
        queryset = Personas.objects.filter(is_delete=False)
        serializer = ReportPersonaSerializer(queryset, many=True)
        serialized_data = serializer.data
        data = pd.DataFrame(serialized_data)
        output_format = request.query_params.get('format', 'csv')
        if output_format == 'excel':
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
            with pd.ExcelWriter(response, engine='openpyxl') as writer:
                data.to_excel(writer, index=False)
        else:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data.csv"'
            data.to_csv(response, index=False)
        return response

class TestApicheck(APIView):
    def post(self, request):
        return Response(
            {"message": "servidor activo."},
            status=status.HTTP_200_OK
        )