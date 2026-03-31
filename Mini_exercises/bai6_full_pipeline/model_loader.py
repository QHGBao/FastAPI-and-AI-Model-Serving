import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "..", "..", "models", "model.pkl")
processor_path = os.path.join(BASE_DIR, "..", "..", "models", "processor.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(processor_path, "rb") as f:
    processor = pickle.load(f)