from . import v1
from ..models import User
from flask import jsonify
from flask_jwt_extended import jwt_required, current_user


@v1.route("/")
def index():
    return jsonify({"hello": "world"})


@v1.route("/profile")
@jwt_required()
def user():
    return jsonify({"id": current_user.id, "username": current_user.username})
