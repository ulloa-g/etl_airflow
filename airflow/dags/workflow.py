import sys
import os

import logging

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta


def setup_logger(log_file):
    """
    Configura un logger para escribir en un archivo.
    """
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    handler.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger


with DAG(
    'etl_pipeline',
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2023, 10, 1),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=5),
    },
    schedule_interval='@daily',
) as dag:
    log_file = '/home/gabriel/repos/etl_airflow/data/pipeline.log'
    logger = setup_logger(log_file)

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract_data,
        op_kwargs={'file_path': '/home/gabriel/repos/etl_airflow/data/raw_titanic_data.csv',
                   'logger': logger},
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform_data,
        op_kwargs={'raw_data': extract_task.output,
                   'logger': logger},
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load_data,
        op_kwargs={'clean_df': transform_task.output,
                   'logger': logger},
    )

    extract_task >> transform_task >> load_task
