from os import access
from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token
from jinja2.runtime import identity
from . import auth
from ..models import User


@auth.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username and password:
        user = User.query.filter_by(username=username).first()
        if not user or not user.verify_password(password):
            return jsonify({"error": "Invalid username or password"}), 401
        access_token = create_access_token(identity=user, fresh=True)
        refresh_token = create_refresh_token(identity=user)
        return jsonify(access_token=access_token, refresh_token=refresh_token)

    return jsonify({"error": "Invalid username or password"}), 401
