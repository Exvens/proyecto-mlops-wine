Proyecto Final 

Integrantes:

Giovanny Obando Duque, 

Javier Eduardo Guerrero Buendia 

Link base de datos: https://drive.google.com/drive/folders/1J75ukeq-2yBUYGMQh79ktTFNXWaeHGGJ?usp=sharing

Este repositorio contiene un proyecto end-to-end de Machine Learning Operations (MLOps) desarrollado para automatizar el ciclo de vida de un modelo predictivo, desde el seguimiento de experimentos hasta el despliegue como API.

## 1. Definición del Proyecto (Hipótesis de Negocio)
* *Problema:* Una viña necesita automatizar el control de calidad de sus vinos tintos. Las pruebas de cata humana son costosas, lentas y subjetivas.
* *Solución:* Un modelo de Machine Learning (Random Forest) que predice la calidad del vino (escala del 0 al 10) basándose en características fisicoquímicas (acidez, pH, azúcar, etc.).
* *Métrica de Éxito:* Error Cuadrático Medio (MSE) minimizado (~0.30) y pipeline de entrenamiento y despliegue 100% automatizado.
* *Dataset:* [Red Wine Quality (Kaggle / UC Irvine)](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)

## 2. Tecnologías y Herramientas Utilizadas
* *Lenguaje:* Python 3.13
* *Control de Versiones:* Git & GitHub
* *Experiment Tracking:* MLflow
* *Orquestación de Pipelines:* Prefect
* *Despliegue (API):* FastAPI & Uvicorn
* *Testing y Calidad:* Pytest, Flake8, Black
* *Machine Learning:* Scikit-Learn, Pandas

## 3. Estructura del Repositorio

proyecto-mlops-wine/
├── data/                   # Dataset original (winequality-red.csv)
├── docs/                   # Documentación adicional
├── models/                 # Modelos serializados (.joblib)
├── notebooks/              # Cuadernos Jupyter (EDA y Baseline) y base de datos de MLflow
├── src/                    # Código fuente
│   ├── api/                # Código de FastAPI (main.py)
│   └── models/             # Pipeline de entrenamiento de Prefect
├── tests/                  # Pruebas automatizadas (pytest)
├── README.md               # Este archivo
└── requirements.txt        # Dependencias del proyecto


## 4. Instrucciones de Reproducción

### 4.1. Configuración del Entorno
Clona el repositorio y crea un entorno virtual:

git clone https://github.com/Exvens/proyecto-mlops-wine.git
cd proyecto-mlops-wine
python -m venv venv

# Activar entorno (Windows)
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt


### 4.2. Ejecutar el Pipeline de Entrenamiento (Prefect + MLflow)
El pipeline carga los datos, entrena un modelo Random Forest, registra las métricas en MLflow y guarda el modelo .joblib.

python src/models/train_pipeline.py

Para ver los experimentos en MLflow, ejecuta mlflow ui --backend-store-uri sqlite:///notebooks/mlflow.db y abre http://127.0.0.1:5000

### 4.3. Desplegar la API (FastAPI)
Para levantar el servidor web y realizar predicciones en tiempo real:

uvicorn src.api.main:app --reload

Ingresa a http://127.0.0.1:8000/docs en tu navegador para probar la interfaz interactiva (Swagger UI).

### 4.4. Ejecutar Pruebas (Pytest)
Para verificar que la API y el código funcionan correctamente:

python -m pytest


## 5. Monitoreo y Observabilidad (Diseño Propuesto)
Para asegurar que el modelo mantenga su rendimiento en producción, se propone la siguiente arquitectura:

1. *Monitoreo de Infraestructura (FastAPI):*
   * Herramienta: Prometheus + Grafana.
   * Métricas: Latencia de la API (tiempo de respuesta), tasa de errores HTTP (ej. 500s, 400s) y uso de CPU/RAM del contenedor.

2. *Monitoreo del Modelo (Data & Concept Drift):*
   * Herramienta: Evidently AI o Datadog.
   * Métricas: 
     * *Data Drift:* Monitorear si cambian las distribuciones químicas del vino entrante respecto a los datos de entrenamiento.
     * *Concept Drift:* Comparar las predicciones de calidad contra los resultados reales de catas humanas para medir la degradación del MSE en el tiempo.
