#
import pandas as pd
from numpy import split
from sqlalchemy import create_engine

import Code.Utils.utils_db
from Code.Utils.utils_db import *

# Funcion para meter un csv en el datalake
def load_data_in_datalake_from_csv(csv):
    # todo
    # Establecer la conexión al motor de la base de datos PostgreSQL
    engine = create_engine(f'postgresql://postgres:{Code.Utils.utils_db.passw}@{db_ip}:{db_port}/{bd_datalake_poc}')

    # Archivo a utlizar en la POC
    file = csv

    # Obtener el nombre de la tabla a partir del nombre del archivo CSV
    global table_name
    table_name = split(file)[0]


    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(csv)

    # Crear la tabla en PostgreSQL y cargar los datos
    df.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"Datos de '{table_name}' cargados en la base de datos.")

# Funcion para recorrer los csv e insertarlos en el datalake
def load_folder_in_datalake(csv):
    # todo
    pass