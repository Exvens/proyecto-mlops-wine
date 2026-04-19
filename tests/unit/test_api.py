from fastapi.testclient import TestClient
from src.api.main import app

# Creamos un cliente falso para hacerle peticiones a nuestra API sin encender el servidor
client = TestClient(app)


def test_predict_endpoint_returns_200():
    """Prueba que el endpoint /predict funciona correctamente con datos válidos."""

    # Simulamos los datos de un vino
    datos_vino_prueba = {
        "fixed_acidity": 7.4,
        "volatile_acidity": 0.7,
        "citric_acid": 0.0,
        "residual_sugar": 1.9,
        "chlorides": 0.076,
        "free_sulfur_dioxide": 11.0,
        "total_sulfur_dioxide": 34.0,
        "density": 0.9978,
        "pH": 3.51,
        "sulphates": 0.56,
        "alcohol": 9.4,
    }

    # Hacemos una petición POST falsa a nuestra API
    response = client.post("/predict", json=datos_vino_prueba)

    # Comprobamos que la respuesta sea exitosa (200)
    assert response.status_code == 200

    # Comprobamos que la respuesta contenga la palabra clave esperada
    assert "calidad_estimada_del_vino" in response.json()
