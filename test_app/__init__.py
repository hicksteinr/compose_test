import os
from flask import Flask
from flask_pymongo import pymongo
from flask import render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    return app


app = create_app()

CONNECTION_STRING = os.getenv("DB_URI")
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database("users")


our_mongos = [
    {"db": "not a db", "collection": "not a collection"},
    {"db": db, "collection": db.get_collection("test")},
]


@app.route("/")
@app.route("/hello")
def hello():
    return render_template("hello.html", our_mongos=our_mongos)
