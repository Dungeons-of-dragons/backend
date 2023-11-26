import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or "Hellosdfjkhwuieycriowhsdujfhvweuidrbyweuistv8weuc0r9wiq0m9w34uc589342c4mi239ui0rm9245u0t"
    )
    JWT_SECRET_KEY = (
        os.environ.get("JWT_SECRET_KEY")
        or "jwtskjioejrcweirudiwuxnweyxr7nytuwxrueiyrweuirurtyweuxmrxumtyuwmyiytmy"
    )
    JWT_COOKIE_SECURE = False
    # JWT_TOKEN_LOCATION = ['cookie','headers']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DEV_DB")
        or f"sqlite:///{os.path.join(basedir, 'data-dev.sqlite3')}"
    )


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("TEST_DB")
        or f"sqlite:///{os.path.join(basedir, 'data-test.sqlite3')}"
    )


config = {"dev": DevConfig, "test": TestConfig, "default": DevConfig}
