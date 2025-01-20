from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    color = os.getenv("COLOR", "red")
    user_count = 42  # Simulating user count
    return render_template("index.html", color=color, user_count=user_count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

