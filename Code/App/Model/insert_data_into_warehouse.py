import pandas as pd
from sqlalchemy import create_engine

import Code.Utils.utils_db
from Code.Utils.utils_db import *

# Función para cargar los datos en el almacén de datos desde un DataFrame
def load_data_into_warehouse_from_df(df):
    # Transformación: seleccionar las variables relevantes
    df_relevant = df[['game_id', 'competition_id', 'season', 'home_club_name', 'away_club_name', 'home_club_goals', 'away_club_goals', 'result_1x2']]
    return df_relevant

# Función para insertar datos en el almacén de datos
def insert_data_into_warehouse(df_relevant):
    # Establecer la conexión al motor de la base de datos PostgreSQL
    engine = create_engine(f'postgresql://postgres:{Code.Utils.utils_db.passw}@{db_ip}:{db_port}/{bd_warehouse_poc}')

    # Insertar los datos en el almacén de datos
    df_relevant.to_sql('games', engine, if_exists='replace', index=False)

    print("Datos insertados en el almacén de datos (Data Warehouse).")
