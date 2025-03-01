import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1  # Defined here to avoid NameError


def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5 # Adds points to the user's score based on game difficulty.

    file_path = os.path.abspath(SCORES_FILE_NAME)
    print(f"Saving scores to: {file_path}") # Print the absolute path for debugging

    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read().strip() or 0)
        else:
            current_score = 0

        new_score = current_score + POINTS_OF_WINNING
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))
    except Exception as e:
        print(f"Error updating score: {e}")
        return BAD_RETURN_CODE
