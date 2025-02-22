import random
import requests

def get_money_interval(difficulty, usd_amount):
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        response.raise_for_status()
        rate = response.json().get("rates", {}).get("ILS", 3.5)
    except:
        rate = 3.5

    exact_value = usd_amount * rate
    margin = 5 - difficulty
    return exact_value - margin, exact_value + margin

def get_guess_from_user(usd_amount):
    while True:
        try:
            return float(input(f"Guess the value of {usd_amount} USD in ILS: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def play(difficulty):
    usd_amount = random.randint(1, 100)
    min_val, max_val = get_money_interval(difficulty, usd_amount)
    user_guess = get_guess_from_user(usd_amount)

    if min_val <= user_guess <= max_val:
        print("Correct! You guessed within the allowed range.")
        return True
    else:
        print(f"Wrong! The correct value was between {min_val:.2f} and {max_val:.2f}.")
        return False
