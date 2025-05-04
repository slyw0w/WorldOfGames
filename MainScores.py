import os
from flask import Flask

app = Flask(__name__)

SCORES_FILE_NAME = "Scores.txt"

def read_score():
    # Reads the current score from the Scores.txt file.
    file_path = os.path.abspath(SCORES_FILE_NAME)
    print(f"Reading scores from: {file_path}")  # Print path for debugging

    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read().strip()
            if not score:  # If the file is empty
                raise ValueError("File is empty")
            return score
    except Exception as e:
        print(f"Error reading score: {e}")  # Debugging
        return None

@app.route('/')
def score_server():
    score = read_score()
    if score is not None:
        return f"""
        <html>
            <head><title>Scores Game</title></head>
            <body><h1>The score is <div id="score">{score}</div></h1></body>
        </html>
        """
    else:
        return f"""
        <html>
            <head><title>Scores Game</title></head>
            <body><h1><div id="score" style='color:red'>Error reading score</div></h1></body>
        </html>
        """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8777)
