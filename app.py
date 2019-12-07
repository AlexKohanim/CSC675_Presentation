#!/usr/bin/env python3
from flask import Flask, blueprints
import pymysql
from views.index import index_blueprint

app = Flask(__name__)

app.register_blueprint(index_blueprint)

if __name__ == "__main__":
    app.run("0.0.0.0")
