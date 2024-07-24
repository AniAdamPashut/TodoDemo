import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello, World"


PORT = os.environ["PORT"]
HOST = os.environ["HOST"]

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)