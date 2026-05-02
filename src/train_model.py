import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
import joblib, os

# Load dataset
df = pd.read_csv("data/gdp_1960_2020.csv")

X = df[["country", "year"]]
y = df["gdp"]

# RandomForest për variacion midis shteteve
preprocessor_rf = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["country"]),
        ("num", "passthrough", ["year"])
    ]
)

rf_model = Pipeline(steps=[
    ("preprocessor", preprocessor_rf),
    ("regressor", RandomForestRegressor(n_estimators=200, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf_model.fit(X_train, y_train)

# LinearRegression për çdo vend veçmas
lin_models = {}
for country in df["country"].unique():
    df_c = df[df["country"] == country]
    lin = LinearRegression()
    lin.fit(df_c[["year"]], df_c["gdp"])
    lin_models[country] = lin

# Save models
os.makedirs("models", exist_ok=True)
joblib.dump(rf_model, "models/gdp_predictor_rf.pkl")
joblib.dump(lin_models, "models/gdp_predictor_lin.pkl")

print("✅ RandomForest + country-specific LinearRegression models saved")
