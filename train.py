import csv
import json
import math
from typing import List, Tuple


class Normalizer:
    def __init__(self, values: list[float]):
        self.min_val = min(values)
        self.max_val = max(values)
        self.range = self.max_val - self.min_val if self.max_val != self.min_val else 1

    def normalize(self, x: float) -> float:
        return (x - self.min_val) / self.range

    def denormalize(self, x: float) -> float:
        return x * self.range + self.min_val


def load_data(filepath: str = "data.csv") -> List[Tuple[float, float]]:
    result: List[Tuple[float, float]] = []
    with open(filepath, "r") as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            km: float = float(row[0])
            price: float = float(row[1])
            result.append((km, price))
    return result


def save_thetas(
    theta0: float,
    theta1: float,
    km_norm: Normalizer,
    price_norm: Normalizer,
    filepath: str = "thetas.json",
):
    with open(filepath, "w") as f:
        json.dump(
            {
                "theta0": theta0,
                "theta1": theta1,
                "km_min": km_norm.min_val,
                "km_max": km_norm.max_val,
                "price_min": price_norm.min_val,
                "price_max": price_norm.max_val,
            },
            f,
        )


def estimate_price(
    km: float, theta0: float, theta1: float, km_norm: Normalizer, price_norm: Normalizer
) -> float:
    km_normalized = km_norm.normalize(km)
    normalized_price = theta0 + (theta1 * km_normalized)
    return price_norm.denormalize(normalized_price)


def train(
    data: List[Tuple[float, float]],
    learning_rate: float = 1e-2,
    iteration: int = 100000,
) -> Tuple[float, float, Normalizer, Normalizer]:
    km_list = [km for km, _ in data]
    price_list = [price for _, price in data]

    km_norm = Normalizer(km_list)
    price_norm = Normalizer(price_list)

    normalized_data = [
        (km_norm.normalize(km), price_norm.normalize(price)) for km, price in data
    ]

    theta0: float = 0.0
    theta1: float = 0.0
    m: int = len(normalized_data)

    for i in range(iteration):
        sum_error0 = 0.0
        sum_error1 = 0.0
        for km, price in normalized_data:
            prediction: float = theta0 + theta1 * km
            error = prediction - price
            sum_error0 += error
            sum_error1 += error * km
        theta0 -= learning_rate * sum_error0 / m
        theta1 -= learning_rate * sum_error1 / m

        if math.isnan(theta0) or math.isnan(theta1):
            print(f"NaN detected at iteration {i}, stopping training")
            break

        if i % 1000 == 0 or i == iteration - 1:
            print(f"Iteration {i}: theta0 = {theta0:.5f}, theta1 = {theta1:.10f}")

    return theta0, theta1, km_norm, price_norm


def main():
    data: List[Tuple[float, float]] = load_data()
    theta0, theta1, km_norm, price_norm = train(data)
    save_thetas(theta0, theta1, km_norm, price_norm)

    estimate_price(50000, theta0, theta1, km_norm, price_norm)


if __name__ == "__main__":
    main()
