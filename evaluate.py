import math
from typing import List, Tuple

from predict import load_thetas
from train import estimate_price, load_data


def evaluate_model():
    data: List[Tuple[float, float]] = load_data()
    theta0, theta1, km_norm, price_norm = load_thetas()

    total_squared_error = 0.0
    total_absolute_error = 0.0

    for km, true_price in data:
        predicted = estimate_price(km, theta0, theta1, km_norm, price_norm)
        error = predicted - true_price
        total_squared_error += error**2
        total_absolute_error += abs(error)

    rmse: float = math.sqrt(total_squared_error / len(data))
    mae: float = total_absolute_error / len(data)

    print(f"RMSE : {rmse:.2f} $")
    print(f"MAE : {mae:.2f} $")


if __name__ == "__main__":
    evaluate_model()
