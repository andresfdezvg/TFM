import psycopg2
import pandas as pd

# Archivo para configurar los datos del warehouse e insertarlos
def load_data_into_warehouse_from_df(df):


# Conectarse a la base de datos
    conn = psycopg2.connect(
    host="localhost",
    database="tfmdatalake_poc",
    user="postgres",
    password="123456"
)

# Crear un cursor para ejecutar consultas SQL
    cur = conn.cursor()

# Ejecutar una consulta para seleccionar los datos específicos de la tabla games
cur.execute("""
    SELECT game_id, season, stadium, home_club_name, away_club_id, result1x2
    FROM games
""")

# Obtener los datos seleccionados
data = cur.fetchall()

# Cerrar el cursor y la conexión
cur.close()
conn.close()

def insert_data_into_warehouse():
    pass