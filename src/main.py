from fastapi import FastAPI
from src.predictions.router import router
from src.predictions.schemas import PredictionRequest
from src.ml.model import predict_price
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