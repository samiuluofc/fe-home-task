"""A Simple script to verify the GET api outputs"""

import requests
import pandas as pd

base_url = 'http://localhost:5000'

resp = requests.get(base_url + '/forecast?date=2021-06-14&time=11:00:00')
print(resp.status_code, resp.text)
resp = requests.get(base_url + '/forecast?date=2021-06-14')
print(resp.status_code, resp.text)
resp = requests.get(base_url + '/forecast')
print(resp.status_code, resp.text)