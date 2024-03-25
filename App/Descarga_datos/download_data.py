import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


def descargar_descomprimir_y_guardar(nombre_conjunto_datos):
    # Directorio donde se guardarán los datos
    directorio_datos = 'datos_kaggle'

    # Comprobamos si el directorio existe, si no, lo creamos
    if not os.path.exists(directorio_datos):
        os.makedirs(directorio_datos)

    # Descargar el archivo zip
    api = KaggleApi()
    api.authenticate()  # Asegúrate de haber configurado tus credenciales de Kaggle
    api.dataset_download_files(nombre_conjunto_datos, path=directorio_datos, unzip=True)

    # Mensaje de confirmación
    print(
        f'Los datos del conjunto {nombre_conjunto_datos} han sido descargados y descomprimidos en {directorio_datos}.')


# Nombre del conjunto de datos en Kaggle
nombre_conjunto_datos = 'davidcariboo/player-scores'  # Reemplaza con el nombre del conjunto que deseas descargar
descargar_descomprimir_y_guardar(nombre_conjunto_datos)
