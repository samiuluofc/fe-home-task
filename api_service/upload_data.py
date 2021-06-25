"""A Simple script to read data from the CSV and verify the POST call"""

import requests
import pandas as pd

base_url = 'http://localhost:5000'
pd_data = pd.read_csv("weatherstats_winnipeg_forecast_hourly.csv")

data = []
for row in pd_data.itertuples():
    data.append({
        "period_string": str(row.period_string),
        "conditions": str(row.conditions),
        "temperature": str(row.temperature),
        "wind_direction": str(row.wind_direction),
        "wind_speed": str(row.wind_speed),
        }
    )

resp = requests.post(
    base_url + '/forecast',
    json={
        'data': data
    },
)
print(resp.status_code, resp.text)