# mlops-iris-pipeline

Paso a paso

Activar el entorno virtual
python -m venv venv && source venv/bin/activate

Instalar los requerimientos. 

pip install -r requirements.txt

Estructura del proyecto.

mlops-iris/
├── airflow/                # DAGs y config de Airflow
│   ├── dags/
│   │   └── iris_pipeline.py
│   └── Dockerfile          # (opcional) si dockerizas Airflow
├── data/                   # Datos crudos y procesados
│   ├── raw/
│   └── processed/
├── models/                 # Modelos serializados
├── src/
│   ├── ingest.py           # ya hecho
│   ├── train.py
│   ├── test.py
│   └── serve.py            # Flask app
├── monitoring/
│   └── monitor_latency.py
├── docker-compose.yml
├── Dockerfile              # para la API Flask
├── requirements.txt
└── README.md
