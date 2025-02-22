import random
import time

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]


def get_list_from_user(difficulty):

    print("\nEnter the numbers you remember, separated by spaces or commas:")
    while True:
        try:
            user_input = list(map(int, input().replace(",", " ").split()))

            if len(user_input) == difficulty:
                return user_input
            else:
                print(f"Invalid input! Please enter exactly {difficulty} numbers.")
        except ValueError:
            print("Invalid input! Please enter only numbers.")

def is_list_equal(sequence, user_sequence):
    return sequence == user_sequence

def play(difficulty):
    sequence = generate_sequence(difficulty)
    print("\nMemorize this sequence:")
    print(sequence)
    time.sleep(0.7)  #show the sequence for 0.7 seconds
    print("c", end="")

    user_sequence = get_list_from_user(difficulty)

    if is_list_equal(sequence, user_sequence):
        print("Well done! You have a great memory!")
        return True
    else:
        print(f"Sorry, that was incorrect. The correct sequence was {sequence}.")
        return False


