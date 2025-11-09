# Dockerfile para proyecto Django
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt ./

# Instala las dependencias
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto 8000 para Gunicorn
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación con Gunicorn
CMD ["gunicorn", "administrador.wsgi:application", "--bind", "0.0.0.0:8000"]
