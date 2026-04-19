import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import mlflow
from prefect import task, flow


@task(name="Cargar y Dividir Datos")
def load_data(file_path: str):
    """Carga los datos y los divide en entrenamiento y prueba."""
    df = pd.read_csv(file_path)
    X = df.drop("quality", axis=1)
    y = df["quality"]
    return train_test_split(X, y, test_size=0.2, random_state=42)


@task(name="Entrenar Modelo Random Forest")
def train_model(X_train, X_test, y_train, y_test):
    """Entrena el modelo y registra todo en MLflow."""
    mlflow.set_tracking_uri("sqlite:///notebooks/mlflow.db")
    mlflow.set_experiment("Proyecto_Vinos_Pipeline")
    mlflow.autolog()

    with mlflow.start_run():
        modelo = RandomForestRegressor(n_estimators=100, random_state=42)
        modelo.fit(X_train, y_train)
        joblib.dump(modelo, "models/modelo_vino.joblib")

        predicciones = modelo.predict(X_test)
        error = mean_squared_error(y_test, predicciones)
        print(f"Error Cuadrático Medio: {error:.4f}")


@flow(name="Pipeline de Entrenamiento de Vinos")
def wine_training_pipeline():
    """El flujo principal que orquesta todo."""
    print("Iniciando el pipeline de entrenamiento...")

    # 1. Cargar datos
    datos = load_data("data/winequality-red.csv")
    X_train, X_test, y_train, y_test = datos

    # 2. Entrenar
    train_model(X_train, X_test, y_train, y_test)

    print("Pipeline finalizado con éxito.")


if __name__ == "__main__":
    wine_training_pipeline()
