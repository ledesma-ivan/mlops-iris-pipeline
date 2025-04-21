import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import os
import mlflow


def load_data(data_path="mlops-iris-pipeline/data/iris_dataset.csv"):
    df = pd.read_csv(data_path)
    X = df.drop("target", axis=1)
    y = df["target"]
    return train_test_split(X, y, test_size=0.2, random_state=42)

    # Aca ya empieza a ser util el modelo que entrenamos


def load_model(model_path="mlops-iris-pipeline/models/iris_rf.pkl"):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Modelo no encontra en {model_path}")
    return joblib.load(model_path)


def evaluate_model(model, X_test, y_test):
    # Realizamos las predicciones y devolvemos la precision + report de
    # clasificacion
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(
        y_test, preds, target_names=[
            "setosa", "versicolor", "virginica"])
    return acc, report


# Definir el nombre del experimento
MLFLOW_EXPERIMENT = "Experimento_test"


def main():
    # 1. Cargamos los datos de prueba

    X_train, X_test, y_train, y_test = load_data()

    # 2. Cargamos el modelo.
    model = load_model()

    # 3. Evaluamos localmente

    acc, report = evaluate_model(model, X_test, y_test)
    print(f"Accuracy en test set: {acc:.4f}")
    print("Classification Report:\n", report)

    # 4. Logeamos en Mlfow
    mlflow.set_experiment(MLFLOW_EXPERIMENT)
    with mlflow.start_run(run_name="test_run"):
        mlflow.log_metric("test_accuracy", acc)

    # Logeamos aca el clasificacion_report como un artefato de texto
        report_path = "mlops-iris-pipeline/models/test_report.txt"

        with open(report_path, "w") as f:
            f.write(report)

        mlflow.log_artifact(report_path, artifact_path="MLFLOW_EXPERIMENT")
        print(
            f"Las metricas y los reportes se ingresaron a MlFlow bajo experimento {MLFLOW_EXPERIMENT}")


if __name__ == "__main__":
    main()
