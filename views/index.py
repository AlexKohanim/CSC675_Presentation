from flask import Blueprint, render_template, session, request


index_blueprint = Blueprint('index', __name__)


@index_blueprint.route("/")
def index():
    return "<h1> <center>Hello World</center> </h1>"
