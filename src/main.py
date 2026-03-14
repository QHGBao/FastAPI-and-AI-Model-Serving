from fastapi import FastAPI
from src.predictions.router import router
from src.predictions.schemas import PredictionRequest
import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import List

app_run = FastAPI(
    title = "FastAPI và AI Model Serving",
    description = "API dự đoán giá nhà",
    version = "1.0"
)

app_run.include_router(
    router = router,
    prefix = "/API/v1",
    tags = ["Predictions"]
)

@app_run.get("/")
def root():
    return {"msg": "FastAPI và AI Model Serving đang hoạt động"}

@app_run.post("/predict")
def predict(data: PredictionRequest):
    return data

# executor = ThreadPoolExecutor()
# @app_run.get("/predict")
# async def predict():
#     loop = asyncio.get_event_loop()
#     return