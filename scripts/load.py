import pandas as pd
import sqlite3

dbpath = '/home/gabriel/repos/etl_airflow/data/titanic.db'
table_name = 'titanic_data'
conn = sqlite3.connect(dbpath)

def load_data(clean_df, logger):
    """
    Carga los datos transformados en una base de datos SQLite.

    Args:
        clean_df (pd.DataFrame): Datos transformados.
        logger (logging.Logger): Logger para registrar información.
    """
    try:
        logger.info("Iniciando carga a base de datos.")
        clean_df.to_sql(table_name, conn, if_exists='replace', index=False)
    except Exception as e:
        logger.error(f"Se produjo un error al cargar los datos: {e}")
    finally:
        logger.info("Carga de datos completada.")
        logger.info(f"Los datos se han cargado en la tabla {table_name} de la base de datos {dbpath}.")
        conn.close()
