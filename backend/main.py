from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app=FastAPI(title="Resale Flat Price API")

# Load model and encoders ONCE
model=joblib.load("best_pipeline.pkl")
uniques=joblib.load("unique_values.pkl")

class InputSchema(BaseModel):
    year: int
    month: int
    town: str
    street_name: str
    flat_type: str
    flat_model: str
    storey_range: str
    floor_area_sqm: float
    remaining_lease: int

@app.post("/predict")
def predict_price(data: InputSchema):

    try:
        month_sin=np.sin(2*np.pi*data.month/12)
        month_cos=np.cos(2*np.pi*data.month/12)

        flat_age=99-data.remaining_lease

        input_df=pd.DataFrame([{
            "year": data.year,
            "month_sin": month_sin,
            "month_cos":month_cos,
            "town": data.town,
            "street_name":data.street_name,
            "flat_type": data.flat_type,
            "flat_model": data.flat_model,
            "storey_range": data.storey_range,
            "floor_area_sqm": data.floor_area_sqm,
            "remaining_lease": data.remaining_lease,
            "flat_age":flat_age
        }])

        if hasattr(model, "feature_names_in_"):
            input_df = input_df[model.feature_names_in_]

        prediction=model.predict(input_df)[0]

        return {"prediction_price": int(prediction)}
    
    except Exception as e:
        return {"error":str(e)}
