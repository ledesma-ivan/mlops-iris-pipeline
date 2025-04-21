import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import os

def load_data():
    df = pd.read_csv("mlops-iris-pipeline/data/iris_dataset.csv")
    X = df.drop("target", axis=1)
    y = df["target"]
    return train_test_split(X, y, test_size=0.2, random_state=42)


    # Aca ya empieza a ser util el modelo que entrenamos 
def load_model(model_path="mlops-iris-pipeline/models/iris_rf.pkl"):
    if not os.path.exists
# TODO: Avanzar con el load_model