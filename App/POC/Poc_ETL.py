import os
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

def calculate_1X2(home, away):
    home = int(home)
    away = int(away)
    if(home > away):
        return '1'
    elif(away > home):
        return '2'
    else:
        return 'X'

def poc_etl():
    # INSERTAR LOS DATOS CRUDOS AL DATALAKE
    # Establecer la conexión al motor de la base de datos PostgreSQL
    passw = input("Introduce la clave de la base de datos para poc_etl: ")
    engine = create_engine(f'postgresql://postgres:{passw}@127.0.0.1:5432/tfmdatalake_poc')

    # Directorio donde se encuentran los archivos CSV
    csv_directory = 'C:/Users/Andres/Desktop/Datos TFM/CSV'

    file = 'games.csv'

    # Iterar sobre los archivos CSV y cargar los datos en la base de datos
    # Obtener el nombre de la tabla a partir del nombre del archivo CSV
    table_name = os.path.splitext(file)[0]

    # Ruta completa del archivo CSV
    csv_path = os.path.join(csv_directory, file)

    # Cargar el archivo CSV en un DataFrame
    df_games = pd.read_csv(csv_path)

    # Crear la tabla en PostgreSQL y cargar los datos
    df_games.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"Datos de '{table_name}' cargados en la base de datos.")

    # PRUEBA DE PROCESO ETL
    # Eliminar los valores null
    df_games = df_games.dropna()
    print("Datos NaN eliminados")

    # Crear una nueva columna '1X2'
    df_games['result_1x2'] = df_games.apply(lambda row: calculate_1X2(row['home_club_goals'], row['away_club_goals']), axis=1)
    df_games['result_1x2'] = df_games['result_1x2'].astype('category')
    print("Column result_1x2 added")

    # Eliminar el texto de las columnas de formacion
    df_games['home_club_formation'] = df_games['home_club_formation'].apply(lambda value: value.split(" ")[0])
    df_games['away_club_formation'] = df_games['away_club_formation'].apply(lambda value: value.split(" ")[0])
    print("Columns home_club_formation and home_club_formation changed")

    # Insertar en warehouse
    engine = create_engine(f'postgresql://postgres:{passw}@127.0.0.1:5432/tfmwarehouse_poc')
    df_games.to_sql(table_name, engine, if_exists='replace', index=False)
    print("Table added to data warehouse")
