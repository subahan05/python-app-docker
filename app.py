from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style="color:red">Python Flask App </h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
