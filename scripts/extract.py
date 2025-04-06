import pandas as pd
import logging


def extract(file_path):
    """
    Extrae datos de un archivo CSV y devuelve un DataFrame de pandas.

    Args:
        file_path (str): La ruta al archivo CSV.

    Returns:
        pd.DataFrame: Los datos extraídos como un DataFrame de pandas.
    """
    logging.info(f"Comenzando extracción de datos desde la ruta: {file_path}")
    try:
        raw_data = pd.read_csv(file_path, index_col='PassengerId')
        logging.info(f"Datos extraídos exitosamente.")
        return raw_data
    except FileNotFoundError:
        logging.error(f"El archivo no fue encontrado en la ruta: {file_path}")
        return None
    except Exception as e:
        print(f"Se produjo un error al extraer los datos de la ruta: {file_path}: {e}")
        return None


if __name__ == "__main__":
    # Configuración básica del logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    file_path = '../data/raw_titanic_data.csv'
    raw_data = extract(file_path)
