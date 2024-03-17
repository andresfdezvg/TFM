# Main file
from App.Descarga_datos.download_data import descargar_descomprimir_y_guardar
from App.POC.Poc_ETL import poc_etl
from App.POC.Poc_modelado import poc_modelado


def poc():
    poc_etl()
    poc_modelado()


def download_data():
    # Nombre del conjunto de datos en Kaggle
    nombre_conjunto_datos = 'davidcariboo/player-scores'  # Reemplaza con el nombre del conjunto que deseas descargar
    descargar_descomprimir_y_guardar(nombre_conjunto_datos)


if __name__ == '__main__':
    #poc()
    download_data()

