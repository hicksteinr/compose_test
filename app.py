import time
import os

from flask import Flask
from flask_pymongo import pymongo

app = Flask(__name__, instance_relative_config=True)
app.config()


@app.route("/")
def hello():
    count = 12
    return "Hello ORLDld! I have been seen {} times.\n".format()


if __name__ == "__main__":
    app.run(debug=True, port=8001)
