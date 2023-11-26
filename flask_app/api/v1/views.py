from . import v1
from ..models import User
from flask import jsonify, request
from flask_jwt_extended import jwt_required, current_user
from ..influx import client, bucket, measurement, org
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS
# from app import app


@v1.route("/")
def index():
    return jsonify({"hello": "world"})


@v1.route("/profile")
@jwt_required()
def user():
    return jsonify({"id": current_user.id, "username": current_user.username})


@v1.route("/lights", methods=["POST"])
def lights():
    state = request.json.get("light", None)
    if state is not None:
        # print(state)
        write_client = client.write_api(write_options=SYNCHRONOUS)

        point = Point(measurement).tag("lights", "state").field("light", state)
        write_client.write(bucket=bucket, org=org, record=point)
        return jsonify({"light": state})
    return jsonify({'error': 'Invalid Options'}), 400

    # if (state):
