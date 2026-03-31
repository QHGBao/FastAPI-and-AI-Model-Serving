from fastapi import FastAPI
from typing import List
from schemas import PredictionRequest
from service import make_batch_prediction

app = FastAPI()

@app.post("/predict")
def predict(requests: List[PredictionRequest]):
    return make_batch_prediction(requests)

@app.get("/")
def root():
    return {"message": "API is running"}