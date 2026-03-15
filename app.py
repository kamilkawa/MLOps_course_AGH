import numpy as np
from fastapi import FastAPI
from inference import load_model, predict
from api.models.iris import PredictRequest, PredictResponse

app = FastAPI()
model = load_model()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict_endpoint(request: PredictRequest) -> PredictResponse:
    data = np.array(
        [
            [
                request.sepal_length,
                request.sepal_width,
                request.petal_length,
                request.petal_width,
            ]
        ]
    )
    result = predict(model, data)
    return PredictResponse(prediction=result[0])
