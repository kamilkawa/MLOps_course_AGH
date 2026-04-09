import numpy as np
import joblib
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


def load_model(path: str = "model.joblib") -> DecisionTreeClassifier:
    return joblib.load(path)


def predict(model: DecisionTreeClassifier, data: np.ndarray) -> list[str]:
    iris = load_iris()
    prediction = model.predict(data)
    return [iris.target_names[p] for p in prediction]
