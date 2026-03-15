import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib


def load_data() -> tuple[np.ndarray, np.ndarray]:
    dataset = load_iris()
    return dataset.data, dataset.target


# Classification problem
def train_model() -> DecisionTreeClassifier:
    X, y = load_data()
    model = DecisionTreeClassifier()
    model.fit(X, y)
    return model


def save_model(model: DecisionTreeClassifier, path: str = "model.joblib") -> None:
    joblib.dump(model, path)


# TODO: Maybe put that into some kind of pipeline in app/backend? Now I have to execute that training + inference manually
# uv run python training.py - to create and 'register' the model
if __name__ == "__main__":
    model = train_model()
    save_model(model)
    print("Model trained and saved.")
