import random

def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {difficulty}: "))
            if 1 <= guess <= difficulty:
                return guess
            else:
                print(f"Invalid input! Please enter a number between 1 and {difficulty}.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def compare_results(secret_number, user_guess):
    return user_guess == secret_number


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)

    if compare_results(secret_number, user_guess):
        print("Congratulations! You guessed correctly!")
        return True
    else:
        print(f"Wrong! The correct number was {secret_number}. Better luck next time!")
        return False
