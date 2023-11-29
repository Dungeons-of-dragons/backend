import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

    # influx config

def get_or_defalult(key, default):
    return os.environ.get(key) or default

InfluxDBConfig={
'INFLUX_ORG' : get_or_defalult('INFLUX_ORG', 'DOD'),
'INFLUX_TOKEN' : os.environ.get('INFLUX_TOKEN'),
'INFLUX_URL' : get_or_defalult('INFLUX_URL', 'http://pie.local:8086'),
'INFLUX_MEASUREMENT' : get_or_defalult('INFLUX_MEASUREMENT', 'dht11'),
'INFLUX_BUCKET' : get_or_defalult('INFLUX_BUCKET', 'testdht'),
}

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or "Hellosdfjkhwuieycriowhsdujfhvweuidrbyweuistv8weuc0r9wiq0m9w34uc589342c4mi239ui0rm9245u0t"
    )

    # JWT config
    JWT_SECRET_KEY = (
        os.environ.get("JWT_SECRET_KEY")
        or "jwtskjioejrcweirudiwuxnweyxr7nytuwxrueiyrweuirurtyweuxmrxumtyuwmyiytmy"
    )
    JWT_COOKIE_SECURE = False
    # JWT_TOKEN_LOCATION = ['cookie','headers']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    # influx config
    INFLUX_ORG = InfluxDBConfig['INFLUX_ORG'] 
    INFLUX_TOKEN = InfluxDBConfig['INFLUX_TOKEN']
    INFLUX_URL = InfluxDBConfig['INFLUX_URL']
    INFLUX_MEASUREMENT = InfluxDBConfig['INFLUX_MEASUREMENT']
    INFLUX_BUCKET = InfluxDBConfig['INFLUX_BUCKET']

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
