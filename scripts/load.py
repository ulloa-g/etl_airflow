import pandas as pd
import sqlite3

dbpath = '/home/gabriel/repos/etl_airflow/data/titanic.db'
table_name = 'titanic_data'
conn = sqlite3.connect(dbpath)

def load_data(clean_df):
    """
    Carga los datos transformados en una base de datos SQLite.

    Args:
        clean_df (pd.DataFrame): Datos transformados.
    """
    try:
        clean_df.to_sql(table_name, conn, if_exists='replace', index=False)
    except Exception as e:
        print(f"Se produjo un error al cargar los datos: {e}")
    finally:
        conn.close()
