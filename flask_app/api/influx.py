import influxdb_client
from influxdb_client import InfluxDBClient

# from influxdb_client.client.write_api import SYNCHRONOUS
from flask import current_app
from config import InfluxDBConfig


token = InfluxDBConfig["INFLUX_TOKEN"]
org = InfluxDBConfig["INFLUX_ORG"]
url = InfluxDBConfig["INFLUX_URL"]
measurement = InfluxDBConfig["INFLUX_MEASUREMENT"]
bucket = InfluxDBConfig["INFLUX_BUCKET"]

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

query_api = client.query_api()


query=f"""
from(bucket: "{bucket}")
  |> range(start: -120m)
  |> filter(fn: (r) => r["_measurement"] == "measurement1")
  |> filter(fn: (r) => r["_field"] == "light")
  |> filter(fn: (r) => r["lights"] == "state")
"""
temp_query=f"""
        from(bucket: "{bucket}")
          |> range(start: -72h)
          |> filter(fn: (r) => r._measurement == "testdht")
          |> filter(fn: (r) => r._field == "temperature")
"""
tables = query_api.query(temp_query, org="ant")

for t in tables:
    for r in t.records:
        print(r)