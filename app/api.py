from fastapi import FastAPI
from pydantic import BaseModel
from src.predictor import predict_gdp

# Inicializo API
app = FastAPI(title="Global GDP Prediction API")

# Model për input
class GDPRequest(BaseModel):
    country: str
    year: int

# Endpoint për parashikim
@app.post("/predict")
def predict(request: GDPRequest):
    prediction = predict_gdp(request.country, request.year)
    return {
        "country": request.country,
        "year": request.year,
        "predicted_gdp": round(prediction, 2)
    }

# Endpoint testues
@app.get("/")
def root():
    return {"message": "🌍 GDP Prediction API is running!"}
