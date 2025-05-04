from flask import Flask, render_template_string
from Utils import score_server

app = Flask(__name__)

@app.route('/')
def home():
    score = score_server()
    return render_template_string("""
        <html>
            <head><title>World of Games</title></head>
            <body>
                <h1>Welcome to World of Games</h1>
                <div id="score">{{ score }}</div>
            </body>
        </html>
    """, score=score)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8777)
