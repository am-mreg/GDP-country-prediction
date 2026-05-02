import matplotlib.pyplot as plt
import seaborn as sns

def plot_prediction_vs_real(y_test, y_pred):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=y_test, y=y_pred)
    plt.xlabel("Real GDP")
    plt.ylabel("Predicted GDP")
    plt.title("GDP Prediction Performance")
    plt.show()

def plot_country_gdp(country, years, predictions):
    plt.figure(figsize=(10,6))
    plt.plot(years, predictions, marker="o", color="blue")
    plt.title(f"GDP Predictions for {country}")
    plt.xlabel("Year")
    plt.ylabel("GDP (USD)")
    plt.grid(True)
    plt.show()
