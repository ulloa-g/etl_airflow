import sys
import os

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

from scripts.extract import extract_data
from scripts.transform import transform_data

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

with DAG(
    'etl_pipeline',
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2023, 10, 1),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=20),
    },
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract_data,
        op_kwargs={'file_path': '../data/raw_titanic_data.csv'},
    )
    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform_data,
        op_kwargs={'raw_data': '{{ task_instance.xcom_pull(task_ids="extract") }}'},
    )

    extract_task >> transform_task
