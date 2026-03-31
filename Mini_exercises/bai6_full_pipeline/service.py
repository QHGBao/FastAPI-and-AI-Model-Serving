import pandas as pd
import numpy as np
from typing import List
from schemas import PredictionRequest
from model_loader import model, processor

FEATURE = [
    "area", "bedrooms", "bathrooms", "floors",
    "property_type", "furniture", "legal_status", "distance_to_center"
]


def predict_batch_price(df: pd.DataFrame):
    input_data = processor.transform(df)
    preds = model.predict(input_data)
    prices = np.expm1(preds)
    return prices


def make_batch_prediction(requests: List[PredictionRequest]):
    data = []

    for req in requests:
        data.append(req.model_dump())

    df = pd.DataFrame(data)[FEATURE]
    preds = predict_batch_price(df)

    results = []
    for i, p in enumerate(preds):
        results.append({
            "features": data[i],
            "price": float(p)
        })

    return results