from Live import load_game, welcome
import CurrencyRouletteGame
import MemoryGame
import GuessGame


if __name__ == "__main__":
    print(welcome(input("Please enter your name: ")))
    chosen_game, difficulty = load_game()

    if chosen_game == 1:
        MemoryGame.play(difficulty)
    elif chosen_game == 2:
        GuessGame.play(difficulty)
    elif chosen_game == 3:
        CurrencyRouletteGame.play(difficulty)
