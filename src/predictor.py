import joblib, os
import pandas as pd

rf_model = joblib.load(os.path.join("models", "gdp_predictor_rf.pkl"))
lin_models = joblib.load(os.path.join("models", "gdp_predictor_lin.pkl"))

def predict_gdp(country: str, year: int) -> float:
    if year <= 2020:
        X_new = pd.DataFrame([[country, year]], columns=["country", "year"])
        return rf_model.predict(X_new)[0]
    else:
        if country in lin_models:
            return lin_models[country].predict(pd.DataFrame([[year]], columns=["year"]))[0]
        else:
            # fallback në LinearRegression global
            return rf_model.predict(pd.DataFrame([[country, 2020]], columns=["country", "year"]))[0]
