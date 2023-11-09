from . import v1
from flask import jsonify


@v1.route("/")
def index():
    return jsonify({"hello": "world"})
