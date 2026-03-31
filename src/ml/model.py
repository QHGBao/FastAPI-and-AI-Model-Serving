import numpy as np
import pandas as pd



def predict_batch_price(df: pd.DataFrame, model, processor):
    input = processor.transform(df)
    preds = model.predict(input)
    prices = np.expm1(preds)
    return prices
