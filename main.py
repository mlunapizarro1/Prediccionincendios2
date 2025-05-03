from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model/fire_model.pkl")

class InputData(BaseModel):
    temp: float
    humidity: float
    wind: float
    precipitation: float
    ndvi: float

@app.post("/predict")
def predict_fire(data: InputData):
    input_array = np.array([[data.temp, data.humidity, data.wind, data.precipitation, data.ndvi]])
    prob = model.predict_proba(input_array)[0][1]
    return {"risk_score": round(prob * 100, 2), "risk_level": risk_label(prob)}

def risk_label(prob):
    if prob > 0.7:
        return "ALTO"
    elif prob > 0.4:
        return "MEDIO"
    else:
        return "BAJO"
