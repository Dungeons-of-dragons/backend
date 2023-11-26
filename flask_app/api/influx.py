import influxdb_client
from influxdb_client import InfluxDBClient

# from influxdb_client.client.write_api import SYNCHRONOUS
from flask import current_app
# from app import app
from config import InfluxDBConfig

# with current_app().app_context():
# app.app_context().push()
token = InfluxDBConfig["INFLUX_TOKEN"]
org = InfluxDBConfig["INFLUX_ORG"]
url = InfluxDBConfig["INFLUX_URL"]
measurement = InfluxDBConfig["INFLUX_MEASUREMENT"]
bucket = InfluxDBConfig["INFLUX_BUCKET"]

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

query_api = client.query_api()

# query="""
# from(bucket: "smarthome")
# |>range(start: -30m)
# |>filter(fn: (r)=> r._measurement == "measurement1")
# """
query="""
from(bucket: "smarthome")
  |> range(start: -120m)
  |> filter(fn: (r) => r["_measurement"] == "measurement1")
  |> filter(fn: (r) => r["_field"] == "light")
  |> filter(fn: (r) => r["lights"] == "state")
"""
tables = query_api.query(query, org="ant")

for t in tables:
    for r in t.records:
        print(r)