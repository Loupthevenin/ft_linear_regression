import json
import os
from typing import Tuple


class Normalizer:
    def __init__(self, min_val: float, max_val: float):
        self.min_val = min_val
        self.max_val = max_val
        self.range = self.max_val - self.min_val if self.max_val != self.min_val else 1

    def normalize(self, x: float) -> float:
        return (x - self.min_val) / self.range

    def denormalize(self, x: float) -> float:
        return x * self.range + self.min_val


def estimate_price(
    km: float, theta0: float, theta1: float, km_norm: Normalizer, price_norm: Normalizer
) -> float:
    km_normalized = km_norm.normalize(km)
    price_normalized = theta0 + (theta1 * km_normalized)
    return price_norm.denormalize(price_normalized)


def load_thetas(
    filepath: str = "thetas.json",
) -> Tuple[float, float, Normalizer, Normalizer]:
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                theta0: float = float(data.get("theta0", 0.0))
                theta1: float = float(data.get("theta1", 0.0))
                km_norm: Normalizer = Normalizer(
                    float(data["km_min"]), float(data["km_max"])
                )
                price_norm: Normalizer = Normalizer(
                    float(data["price_min"]), float(data["price_max"])
                )
                return theta0, theta1, km_norm, price_norm
        except (json.JSONDecodeError, ValueError):
            print("Erreur de lecture dans thetas.json, valeurs par défaut.")
    return 0.0, 0.0, Normalizer(0, 1), Normalizer(0, 1)


# TODO: Attention au SIGINT
def get_user_input() -> float:
    while True:
        try:
            km_input: str = input("Enter km: ")
            km: float = float(km_input)
            if km < 0:
                print("Ne peut pas etre négatif")
                continue
            return km
        except ValueError:
            print("Entrer un nombre valide.")
        except KeyboardInterrupt:
            print("\nInterruption par l'utilisateur. Sortie du programme.")
            exit(0)


if __name__ == "__main__":
    km: float = get_user_input()

    theta0, theta1, km_norm, price_norm = load_thetas()

    if km < km_norm.min_val or km > km_norm.max_val:
        print("⚠️  Avertissement : la valeur de km est hors des données d'entraînement.")

    price: float = estimate_price(km, theta0, theta1, km_norm, price_norm)
    print(f"km_min: {km_norm.min_val}, km_max: {km_norm.max_val}")
    print("Test prédictions extrêmes:")
    print(
        "km min:",
        km_norm.min_val,
        "-> prix estimé:",
        estimate_price(km_norm.min_val, theta0, theta1, km_norm, price_norm),
    )
    print(
        "km max:",
        km_norm.max_val,
        "-> prix estimé:",
        estimate_price(km_norm.max_val, theta0, theta1, km_norm, price_norm),
    )
    print(f"Estimate price : {price:.2f}")
