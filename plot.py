import matplotlib.pyplot as plt
from typing import List, Tuple
from predict import load_thetas, estimate_price
from train import load_data


def plot_data_and_model():
    data: List[Tuple[float, float]] = load_data()
    km_values = [km for km, _ in data]
    price_values = [price for _, price in data]

    theta0, theta1, km_norm, price_norm = load_thetas()

    km_range = list(range(int(min(km_values)), int(max(km_values)), 1000))
    predicted_prices = [
        estimate_price(km, theta0, theta1, km_norm, price_norm) for km in km_range
    ]

    plt.scatter(km_values, price_values, color="blue", label="Données")
    plt.plot(km_range, predicted_prices, color="red", label="Régression")

    plt.xlabel("Kilométrage (km)")
    plt.ylabel("Prix")
    plt.title("Régression linéaire : Prix en fonction du kilométrage")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_data_and_model()
