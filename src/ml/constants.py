from pathlib import Path

MODEL_PATH = Path("models/model.pkl")

PROCESSOR_PATH = Path("models/processor.pkl")

MODEL_NAME = "house_price_model"

MODEL_VERSION = "1.0"

FEATURE = [
    "area",
    "bedrooms",
    "bathrooms",
    "floors",
    "property_type",
    "furniture",
    "legal_status",
    "distance_to_center"
]
