import os
import shutil
from datetime import datetime

ruta_origen = '.'

# Ruta base donde se moverán los archivos
ruta_destino = './nuev'

# Crear la carpeta de destino si no existe
if not os.path.exists(ruta_destino):
    os.makedirs(ruta_destino)

# Función para extraer la fecha del nombre del archivo
def extraer_fecha(nombre_archivo):
    # Buscar la parte que contiene la fecha en el formato _ddmmaa_
    partes = nombre_archivo.split('_')
    for parte in partes:
        if len(parte) == 6 and parte.isdigit():
            return parte
    return None #240826

# Iterar sobre los archivos en la carpeta de origen
for archivo in os.listdir(ruta_origen):
    if os.path.isfile(os.path.join(ruta_origen, archivo)):
        # Extraer la fecha del nombre del archivo
        fecha_str = extraer_fecha(archivo)
        if fecha_str:
            # Convertir la fecha a un objeto datetime
            fecha = datetime.strptime(fecha_str, '%y%m%d')

            # Obtener el nombre del mes y el año
            nombre_mes = fecha.strftime('%B_%Y')  # Ejemplo: 'September_2024'

            # Crear la carpeta para ese mes si no existe
            carpeta_mes = os.path.join(ruta_destino, nombre_mes)
            if not os.path.exists(carpeta_mes):
                os.makedirs(carpeta_mes)

            # Mover el archivo a la carpeta correspondiente
            archivo_origen = os.path.join(ruta_origen, archivo)
            archivo_destino = os.path.join(carpeta_mes, archivo)
            shutil.move(archivo_origen, archivo_destino)
            print(f'Movido: {archivo} a {carpeta_mes}')
        else:
            print(f'Fecha no encontrada en el archivo: {archivo}')