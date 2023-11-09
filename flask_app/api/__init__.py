from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask import Flask

migrate = Migrate()
sql = SQLAlchemy()
jwt = JWTManager()


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    sql.init_app(app)
    migrate.init_app(app, sql)
    jwt.init_app(app)

    from .v1 import v1

    app.register_blueprint(v1)
    return app
