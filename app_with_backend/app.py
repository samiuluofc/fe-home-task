import requests
import json
from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta

BASE_URL = 'http://api:5000'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    data = {}
    head = []
    display = 'na'
    if request.method == 'POST':
        date = request.form.get('date_pick')
        time = request.form.get('time_pick')
        head =['Day', 'Condition', 'Temperature' , 'Wind speed', 'Wind direction']
        if date != '':
            if time != '':
                resp = requests.get(BASE_URL + '/forecast?date='+ date + '&time=' + time)
                data = json.loads(resp.text)
                display = 'table'
            else:
                resp = requests.get(BASE_URL + '/forecast?date='+ date)
                data = json.loads(resp.text)
                display = 'chart'
        else:
            display = 'error'
            
    return render_template('home.html', head=head, data=data, display=display)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
