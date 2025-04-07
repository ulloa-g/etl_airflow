import pandas as pd


def transform_data(raw_data):
    """
    Transforma los datos crudos del Titanic para su análisis.

    Args:
        raw_data (pd.DataFrame): Datos crudos del Titanic.

    Returns:
        clean_data (pd.DataFrame): Datos transformados.
    """

    # Eliminar columnas innecesarias
    raw_data.drop(columns=["Cabin", "SibSp", "Parch"], inplace=True)

    # Manejo de valores nulos
    raw_data.fillna({"Age": raw_data["Age"].mean(),
                    "Fare": raw_data["Fare"].mean(),
                    }, inplace=True)
    return raw_data
