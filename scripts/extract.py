import pandas as pd
import logging


def extract_data(file_path, logger):
    """
    Extrae datos de un archivo CSV y devuelve un DataFrame de pandas.

    Args:
        file_path (str): La ruta al archivo CSV.
        logger (logging.Logger): Logger para registrar información.

    Returns:
        pd.DataFrame: Los datos extraídos como un DataFrame de pandas.
    """
    logger.info(f"Comenzando extracción de datos desde la ruta: {file_path}")
    try:
        raw_data = pd.read_csv(file_path, index_col='PassengerId')
        logger.info(f"Datos extraídos exitosamente.")
        return raw_data
    except FileNotFoundError:
        logger.error(f"El archivo no fue encontrado en la ruta: {file_path}")
        return None
    except Exception as e:
        logger.error(f"Se produjo un error al extraer los datos: {e}")
        return None
