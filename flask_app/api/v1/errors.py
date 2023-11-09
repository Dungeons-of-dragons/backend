from werkzeug.wrappers import response
from . import v1
from flask import jsonify


@v1.app_errorhandler(404)
def page_not_found(e):
    # print(e.__str__)
    # jsonify(e)
    response = jsonify({"error": "Page not found"})
    response.status_code = 404
    return response


@v1.app_errorhandler(500)
def internal_server(e):
    response = jsonify({"error": "Internal Server"})
    response.status_code = 500
    return response
