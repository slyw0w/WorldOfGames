def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."

def load_game():
    print("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS.""")

    while True:
        try:
            chosen_game = int(input("Enter game number (1-3): "))
            if 1 <= chosen_game <= 3:
                break
            else:
                print("Invalid input! Please choose a number between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print("\nPlease choose game difficulty from 1 to 5:")
    while True:
        try:
            difficulty = int(input("Enter difficulty level (1-5): "))
            if 1 <= difficulty <= 5:
                break
            else:
                print("Invalid input! Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    return chosen_game, difficulty






