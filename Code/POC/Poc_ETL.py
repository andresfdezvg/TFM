# Archivo para la prueba de concepto del proceso ETL

import os
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

import Code.Utils.utils_db
from Code.Utils.utils_db import *


# Funcion para calcular el campo 1X2
# Valores de entrada:
#   home: goles del equipo local (string)
#   away: goles del equipo visitante (string)
# Valor de salida:
#   1: victoria del equipo local
#   X: empate
#   2: victoria del equipo visitante
def calculate_1x2(home, away):
    home = int(home)
    away = int(away)
    if home > away:
        return '1'
    elif away > home:
        return '2'
    else:
        return 'X'


df_games = ''
table_name = ''

# Funcion para obtener los datos e insertarlos crudos al datalake
def extract_data():
    # Establecer la conexión al motor de la base de datos PostgreSQL
    engine = create_engine(f'postgresql://postgres:{Code.Utils.utils_db.passw}@{db_ip}:{db_port}/{bd_datalake_poc}')

    # Directorio donde se encuentran los archivos CSV en local
    csv_directory = 'C:/Users/Andres/Desktop/Datos TFM/CSV'

    # Archivo a utlizar en la POC
    file = 'games.csv'

    # Obtener el nombre de la tabla a partir del nombre del archivo CSV
    global table_name
    table_name = os.path.splitext(file)[0]

    # Ruta completa del archivo CSV
    csv_path = os.path.join(csv_directory, file)

    # Cargar el archivo CSV en un DataFrame
    global df_games
    df_games = pd.read_csv(csv_path)

    # Crear la tabla en PostgreSQL y cargar los datos
    df_games.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"Datos de '{table_name}' cargados en la base de datos.")


# Funcion para transformar los datos
def transform_data():
    # Eliminar los valores null
    global df_games
    df_games = df_games.dropna()
    print("Datos NaN eliminados")

    # Crear una nueva columna '1X2'
    df_games['result_1x2'] = df_games.apply(lambda row: calculate_1x2(row['home_club_goals'], row['away_club_goals']), axis=1)
    df_games['result_1x2'] = df_games['result_1x2'].astype('category')
    print("Column result_1x2 added")

    # Eliminar el texto de las columnas de formacion
    df_games['home_club_formation'] = df_games['home_club_formation'].apply(lambda value: value.split(" ")[0])
    df_games['away_club_formation'] = df_games['away_club_formation'].apply(lambda value: value.split(" ")[0])
    print("Columns home_club_formation and home_club_formation changed")


# Funcion para cargar los datos limpios al warehouse
def load_data():
    # Establecer la conexión al motor de la base de datos PostgreSQL
    engine = create_engine(f'postgresql://postgres:{Code.Utils.utils_db.passw}@{db_ip}:{db_port}/{bd_warehouse_poc}')
    global df_games
    global table_name

    # Insertar en el warehouse
    df_games.to_sql(table_name, engine, if_exists='replace', index=False)
    print("Table added to data warehouse")


# Funcion para el proceso completo de POC ETL
def poc_etl():
    extract_data()
    transform_data()
    load_data()