# Pipeline con Airflow
Este proyecto consiste en una implementación de una pipeline de datos utilizando Apache Airflow para la orquestación de los procesos.

## Apache Airflow
Airflow es una plataforma de código abierto (open-source) para definir, programar y monitorear flujos de trabajo de datos (workflows), particularmente pipelines de datos utilizando python y DAGs (Directed Acyclic Graphs). Una interfaz web facilita la gestión del estado de flujos de trabajo.

En este proyecto, se utiliza para automatizar las tareas de extracción, transformación y carga de datos (ETL). 

Aquí puedes aprender más sobre [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/index.html).

## Descripción general
Este proyecto tiene como objetivo el desarrollo de una pipeline completa para el procesamiento de un dataset. Se utiliza `Apache Airflow` para la orquestación de las tareas, que incluyen la lectura de un archivo CSV, la aplicación de transformaciones y limpieza de datos con `Python`, y la carga final en una base de datos `PostgreSQL`. Este flujo de trabajo permite la exploración y el análisis de los datos a través de consultas SQL.

Estructura general del proyecto:
```
.
├── airflow/
│   ├── dags/
│   │   └── workflow.py
├── data/
├── scripts/
|   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Fuentes de datos utilizadas
Puedes descargar el archivo `CSV` desde este repositorio.
```
.
├── data/raw_titanic_data.csv
```
También puedes descargarlo directamente desde [kaggle](https://www.kaggle.com/competitions/titanic/data)
