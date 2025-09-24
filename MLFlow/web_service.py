from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union
import os
import numpy as np
import script_training
import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri(uri=os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:8080"))

class NumbersRequest(BaseModel):
    X_pred: List[float]

class VersionRequest(BaseModel):
    version: int

app = FastAPI()

@app.post("/update-model")
def update_model(data: VersionRequest):
    model_uri = f"models:/tracking-quickstart/{data.version}"
    script_training.lr = mlflow.sklearn.load_model(model_uri)
    return {"message": "Model updated successfully", "version": data.version}


@app.post("/predict")
def predict(payload: NumbersRequest):
    arr = np.asarray([payload.X_pred], dtype=np.float64)  # (1,4)
    result = script_training.lr.predict(arr)
    return {"Prediction": result.tolist()}
