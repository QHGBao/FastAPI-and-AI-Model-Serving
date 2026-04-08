from fastapi import APIRouter
from .schemas import PredictionRequest, PredictionResponse
from .service import make_batch_prediction
from .cache import get_cached, set_cached
from fastapi.concurrency import run_in_threadpool
from typing import List

router = APIRouter()


@router.post("/predict", response_model=List[PredictionResponse])
async def predict(data: List[PredictionRequest]):
    if not data:
        return []

    # ── 1. Kiểm tra cache ──────────────────────────────────────────────────
    cached = get_cached(data)
    if cached is not None:
        return cached

    # ── 2. Cache miss → chạy model ────────────────────────────────────────
    result = await run_in_threadpool(make_batch_prediction, data)

    # ── 3. Lưu vào cache ──────────────────────────────────────────────────
    set_cached(data, result)

    return result