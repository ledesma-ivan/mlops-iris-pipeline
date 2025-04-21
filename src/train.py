import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib
import os

MLFLOW_EXPERIMENT = "iris_demo"

# Cargo los datos
def main():
    df = pd.read_csv("mlops-iris-pipeline\data\iris_dataset.csv")
    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Configuro MLflow
    mlflow.set_experiment(MLFLOW_EXPERIMENT)
    with mlflow.start_run():
        # Entreno el modelo
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X_train, y_train)

        # Evaluo el modelo
        preds = clf.predict(X_test)
        acc = accuracy_score(y_test, preds)

        # Registro de las metricas y del modelo
        mlflow.log_param("n_estimadors", 100)
        mlflow.log_metric("acurracy", acc)
        mlflow.sklearn.log_model(clf, "model")

        # Guardo el artefano localmente
        # El artefato se refiere al resultado del proceso que hicimos
        os.makedirs("models", exist_ok=True)
        joblib.dump(clf, "mlops-iris-pipeline/models/iris_rf.pkl")
        # .4f establemos el formato que muestre solo 4 decimales nomas.
        print(f"Run ID: {mlflow.active_run().info.run_id} – Accuracy: {acc:.4f}")

if __name__ == "__main__":
    main()