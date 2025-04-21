# MLOps Iris Pipeline

## Paso a paso

### 1. Activar el entorno virtual
```
python -m venv venv
source venv/bin/activate
```

### 2. Instalar los requerimientos
```
pip install -r requirements.txt
```

## Estructura del proyecto
```
mlops-iris/
├── airflow/
│   ├── dags/
│   │   └── iris_pipeline.py       # DAG principal de Airflow
│   └── Dockerfile                 # Imagen de Airflow personalizada
├── data/
│   ├── raw/                      # Datos sin procesar
│   └── processed/                # Datos procesados
├── notebook/
│   └── EDA.ipynb                 # Análisis exploratorio de datos
├── models/                       # Modelos entrenados
├── src/
│   ├── ingest.py                 # Ingesta de datos
│   ├── train.py                  # Entrenamiento del modelo
│   ├── test.py                   # Evaluación del modelo
│   └── serve.py                  # Servir modelo (API u otro)
├── monitoring/
│   └── monitor_latency.py        # Script de monitoreo de latencia
├── docker-compose.yml            # Orquestación de contenedores
├── Dockerfile                    # Dockerfile raíz
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Documentación
```
