import pytest
from src.predictor import predict_gdp

def test_prediction_positive():
    # GDP duhet të jetë pozitive për çdo input
    result = predict_gdp("Albania", 2019)
    assert result > 0, "GDP prediction should be positive"

def test_prediction_type():
    # Rezultati duhet të jetë numerik
    result = predict_gdp("Albania", 2019)
    assert isinstance(result, (float, int)), "Prediction should be a number"

def test_prediction_consistency_rf():
    # RandomForest duhet të japë të njëjtin rezultat për të njëjtin input (<=2020)
    result1 = predict_gdp("Albania", 2019)
    result2 = predict_gdp("Albania", 2019)
    assert result1 == result2, "RF predictions should be consistent for same input"

def test_prediction_future_trend():
    # LinearRegression duhet të japë vlera të ndryshme për vitet pas 2020
    result_2021 = predict_gdp("Albania", 2021)
    result_2025 = predict_gdp("Albania", 2025)
    assert result_2021 != result_2025, "Future predictions should vary by year"
