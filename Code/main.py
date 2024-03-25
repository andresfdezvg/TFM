# Main file
import getpass
from time import sleep

import Code.Utils.utils_db
from Code.App.Model.download_data import descargar_descomprimir_guardar
from Code.POC.Poc_ETL import poc_etl
from Code.POC.Poc_modelado import poc_modelado
from Code.Utils.utils_db import set_password_db


def poc():
    poc_etl()
    poc_modelado()


def download_data():
    # Nombre del conjunto de datos en Kaggle
    nombre_conjunto_datos = 'davidcariboo/player-scores'  # Reemplaza con el nombre del conjunto que deseas descargar
    descargar_descomprimir_guardar(nombre_conjunto_datos)


if __name__ == '__main__':
    # todo: poner input de contraseña
    a = input("Introduce la clave de la base de datos para poc_etl: ")
    set_password_db(a)

    poc()

    # download_data()

