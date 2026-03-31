from fastapi import FastAPI
import pickle
import pandas as pd
import numpy as np
import os

app = FastAPI()

# ===== FIX PATH CHUẨN =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "..", "..", "models", "model.pkl")
processor_path = os.path.join(BASE_DIR, "..", "..", "models", "processor.pkl")

# ===== LOAD MODEL =====
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(processor_path, "rb") as f:
    processor = pickle.load(f)


# ===== FUNCTION PREDICT =====
def predict_batch_price(df: pd.DataFrame):
    input_data = processor.transform(df)
    preds = model.predict(input_data)
    prices = np.expm1(preds)
    return prices


# ===== API =====
@app.post("/predict")
def predict(data: list[dict]):
    df = pd.DataFrame(data)
    preds = predict_batch_price(df)

    return {
        "prices": preds.tolist()
    }

# dùng uvicorn main:app để chạy
