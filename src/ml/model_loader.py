import joblib
from src.ml.constants import MODEL_PATH, PROCESSOR_PATH, MODEL_NAME

model = None
processor = None

def load_model():
    global model, processor
    model = joblib.load(MODEL_PATH)
    processor = joblib.load(PROCESSOR_PATH)
    print(f"Load model {MODEL_NAME} thành công")