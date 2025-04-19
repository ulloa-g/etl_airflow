import pandas as pd
import logging


def transform_data(raw_data, logger):
    """
    Transforma los datos crudos del Titanic para su análisis.

    Args:
        raw_data (pd.DataFrame): Datos crudos del Titanic.
        logger (logging.Logger): Logger para registrar información.

    Returns:
        clean_data (pd.DataFrame): Datos transformados.
    """
    logger.info("Iniciando transformación de datos.")
    try:
        if raw_data is None:
            logger.warning("No se proporcionaron datos para transformar.")
            return None
        
        clean_data = raw_data.copy()

        # Eliminar columnas innecesarias
        clean_data.drop(columns=["Cabin", "SibSp", "Parch"], inplace=True)

        # Manejo de valores nulos
        clean_data.fillna({"Age": clean_data["Age"].mean(),
                           "Fare": clean_data["Fare"].mean(),
                           }, inplace=True)

        # Cambio en filas para mayor claridad
        clean_data.replace({"Embarked": {"S": "Southampton",
                                         "C": "Cherbourg",
                                         "Q": "Queenstown"}}, inplace=True)
        clean_data["Fare"] = clean_data["Fare"].round(2)

        # Renombrar columnas para mayor información
        clean_data.rename(columns={
            "Embarked": "Port",
            "Fare": "Price",
            "Ticket": "TicketNo",
            "Pclass": "TicketClass",
            }, inplace=True)

        logger.info("Transformación de datos completada exitosamente.")
        return clean_data
    except Exception as e:
        logger.error(f"No se pudieron transformar los datos: {e}")
        return None
