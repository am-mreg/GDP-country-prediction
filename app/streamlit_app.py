import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load("models/gdp_predictor.pkl")

st.title("🌍 Global GDP Prediction")

# User input
country = st.text_input("Enter Country", "Albania")
year = st.number_input("Enter Year", min_value=1960, max_value=2050, value=2020)

if st.button("Predict GDP"):
    # Përdor kolonat e sakta sipas dataset-it
    X_new = pd.DataFrame([[country, year]], columns=["country", "year"])
    prediction = model.predict(X_new)[0]
    st.success(f"Predicted GDP for {country} in {year}: {prediction:,.2f} USD")

    # Visualization
    fig, ax = plt.subplots()
    ax.bar([year], [prediction], color="skyblue")
    ax.set_ylabel("GDP (USD)")
    ax.set_title(f"GDP Prediction for {country}")
    st.pyplot(fig)
