import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

import Code.Utils.utils_db
from Code.Utils.utils_db import *


def poc_modelado():
    # Establecer la conexión al motor de la base de datos PostgreSQL
    engine = create_engine(f'postgresql://postgres:{Code.Utils.utils_db.passw}@{db_ip}:{db_port}/{bd_warehouse_poc}')

    # Ejecutar una consulta SELECT y cargar los resultados en un DataFrame
    query = ("SELECT home_club_name, away_club_name, date, home_club_formation, away_club_formation, result_1x2 "
             "FROM games")
    df = pd.read_sql(query, engine)

    # Cambiar la fecha a numero
    df['date'] = df['date'].apply(lambda date_text: int(datetime.strptime(date_text, "%Y-%m-%d").strftime("%Y%m%d")))

    # Convertir las columnas texto a categóricas
    columnas_categoricas = \
        ['home_club_name', 'away_club_name', 'home_club_formation', 'away_club_formation', 'result_1x2']
    for columna in columnas_categoricas:
        df[columna] = df[columna].astype('category')

    # Codificar las categorías como números
    encoder = LabelEncoder()
    for columna in columnas_categoricas:
        df[columna] = encoder.fit_transform(df[columna])

    # Separar las características y la variable objetivo
    x = df.drop(['result_1x2'], axis=1)
    y = df['result_1x2']

    # Dividir los datos en conjunto de entrenamiento y conjunto de prueba
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123)

    # Construir y entrenar el modelo de regresión logística
    modelo = LogisticRegression()
    modelo.fit(x_train, y_train)

    # Evaluar el modelo
    precision = modelo.score(x_test, y_test)
    print("Precisión del modelo:", precision)

    # Guardar los resultados en la base de datos
    resultados = pd.merge(x_test, y_test, left_index=True, right_index=True)
    resultados.to_sql("resultados", engine, if_exists='replace', index=False)
