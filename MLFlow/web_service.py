from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union
import os
import numpy as np
import script_training
import mlflow
import random
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri(uri=os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:8080"))

current_model = mlflow.sklearn.load_model(f"models:/tracking-quickstart/1")
next_model = mlflow.sklearn.load_model(f"models:/tracking-quickstart/1")

class NumbersRequest(BaseModel):
    X_pred: List[float]

class VersionRequest(BaseModel):
    version: int

app = FastAPI()

@app.post("/predict")
def predict(payload: NumbersRequest, p: float = 0.7):
    model = current_model if random.random() < p else next_model
    arr = np.asarray([payload.X_pred], dtype=np.float64)
    result = model.predict(arr)
    return {"Prediction": result.tolist()}


@app.post("/update-model")
def update_model(data: VersionRequest):
    model_uri = f"models:/tracking-quickstart/{data.version}"
    global next_model
    next_model = mlflow.sklearn.load_model(model_uri)
    return {"message": "Next model updated successfully", "version": data.version}

@app.post('/accept-next-model')
def accept_next_model():
    global current_model, next_model
    current_model = next_model
    return {"status": "next model accepted as current"}