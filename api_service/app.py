"""Winnipeg Forecast data API"""
import bson
from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime, timedelta

app = Flask(__name__)
client = MongoClient('db', 27017)
db = client.appdb


@app.route('/forecast', methods=['POST'])
def data_upload():
    """Insert weather data into the NoSQL database"""
    if len(request.json['data']) > 1000:
        return {}, 400
    for e in request.json['data']:
        item = {
            "datetime": datetime.strptime(str(e["period_string"]), "%Y-%m-%d %H:%M:%S"),
            "conditions": str(e["conditions"]),
            "temperature": str(e["temperature"]),
            "wind_direction": str(e["wind_direction"]),
            "wind_speed": str(e["wind_speed"]),
        }
        db.forecast.insert(item)
    
    return {}, 201


@app.route('/forecast', methods=['GET'])
def get_data():
    """Search weather based on date and/or time"""
    start_d = request.args.get('date')
    start_t = request.args.get('time')

    if start_d == None:
        return {}, 422

    data = {}
    if start_t != None:
        start_dt = datetime.strptime(start_d + " " + start_t, "%Y-%m-%d %H:%M:%S")

        for i in range(7): # 7 days
            search_dt = start_dt + timedelta(days=i)
            dts = db.forecast.find_one({"datetime" : search_dt})
            if dts:
                response = {
                    "datetime": dts["datetime"],
                    "conditions": dts["conditions"],
                    "temperature": dts["temperature"],
                    "wind_direction": dts["wind_direction"],
                    "wind_speed": dts["wind_speed"],
                }
                data["day" + str(i)] = [response]
    else:
        for i in range(7): # 7 days
            start_dt = datetime.strptime(start_d + " " + "00:00:00", "%Y-%m-%d %H:%M:%S") + timedelta(days=i)
            end_dt = datetime.strptime(start_d + " " + "23:59:59", "%Y-%m-%d %H:%M:%S") + timedelta(days=i)   
        
            criteria = {"$and": [{"datetime": {"$gte": start_dt, "$lte": end_dt}}]}
            dts = db.forecast.find(criteria)
            if dts:
                response_list = []
                for e in dts:
                    response = {
                        "datetime": e["datetime"],
                        "conditions": e["conditions"],
                        "temperature": e["temperature"],
                        "wind_direction": e["wind_direction"],
                        "wind_speed": e["wind_speed"],
                    }
                    response_list.append(response)
                if response_list:
                    data["day" + str(i)] = response_list
    
    return data, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
