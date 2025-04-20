# mlops-iris-pipeline

Paso a paso

Activar el entorno virtual
python -m venv venv && source venv/bin/activate

Instalar los requerimientos. 

pip install -r requirements.txt

Estructura del proyecto.

mlops-iris/
├── airflow/                
│   ├── dags/
│   │   └── iris_pipeline.py
│   └── Dockerfile          
├── data/                   
│   ├── raw/
│   └── processed/
├── notebook/   
│   ├── EDA.IPYNB
├── models/                
├── src/
│   ├── ingest.py           
│   ├── train.py
│   ├── test.py
│   └── serve.py           
├── monitoring/
│   └── monitor_latency.py
├── docker-compose.yml
├── Dockerfile              
├── requirements.txt
└── README.md
