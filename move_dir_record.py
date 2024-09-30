import os
import shutil
from datetime import datetime
from pathlib import Path

path_source = Path('.')
# Ruta base donde se moverán los archivos
path_destiny = Path('./records')

# Crear la carpeta de destino si no existe
path_destiny.mkdir(parents=True, exist_ok=True)


# Función para extraer la fecha del nombre del archivo
def extraer_fecha(nombre_archivo):
    # Buscar la parte que contiene la fecha en el formato _ddmmaa_
    partes = nombre_archivo.split('_')
    for parte in partes:
        if len(parte) == 6 and parte.isdigit():
            return parte
    return None  # 240826


def get_contact_name(nombre_archivo):
    parts = nombre_archivo.split('_')
    if len(parts) >= 1:
        return parts[0].replace('Grabación de llamada ', '').replace('Call recording ', '')
    return "Desconocido"


# Iterar sobre los archivos en la carpeta de origen
for archivo in path_source.iterdir():
    if archivo.is_file():
        # Extraer la fecha del nombre del archivo
        fecha_str = extraer_fecha(archivo.name)
        if fecha_str:
            try:
                # Convertir la fecha a un objeto datetime
                fecha = datetime.strptime(fecha_str, '%y%m%d')
                # Obtener el nombre del mes y el año
                nombre_mes = fecha.strftime('%Y/%B')  # Ejemplo: '2024/September'

                # Obtener el nombre del contacto
                contact_name = get_contact_name(archivo.name)

                carpeta_mes = path_destiny / nombre_mes / contact_name
                # Crear la carpeta para ese mes si no existe
                carpeta_mes.mkdir(parents=True, exist_ok=True)
                archivo_destino = carpeta_mes / archivo.name
                shutil.move(str(archivo), str(archivo_destino))
                print(f'Movido: {archivo.name} a {carpeta_mes}')
            except Exception as e:
                print(f'Error moviendo el archivo {archivo.name}: {e}')
        else:
            print(f'Fecha no encontrada en el archivo: {archivo.name}')
