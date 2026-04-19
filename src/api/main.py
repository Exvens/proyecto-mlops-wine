from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Crear la aplicación API
app = FastAPI(
    title="API de Calidad de Vinos", description="Predice la calidad del vino tinto"
)

# Cargar nuestro modelo entrenado
modelo = joblib.load("models/modelo_vino.joblib")


# Definir los datos exactos que el usuario debe enviarnos
class WineFeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float


# Crear la ruta (endpoint) donde recibiremos los datos
@app.post("/predict")
def predict_quality(wine: WineFeatures):
    # Organizar los datos en el mismo orden que aprendió el modelo
    datos = [
        [
            wine.fixed_acidity,
            wine.volatile_acidity,
            wine.citric_acid,
            wine.residual_sugar,
            wine.chlorides,
            wine.free_sulfur_dioxide,
            wine.total_sulfur_dioxide,
            wine.density,
            wine.pH,
            wine.sulphates,
            wine.alcohol,
        ]
    ]

    # Hacer la predicción
    prediccion = modelo.predict(datos)

    # Devolver el resultado (redondeado a 2 decimales)
    return {"calidad_estimada_del_vino": round(prediccion[0], 2)}
