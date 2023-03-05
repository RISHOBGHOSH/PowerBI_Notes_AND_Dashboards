# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
from datetime import datetime

import requests
import time
import random

##class for data_generation


def data_generation():
    surr_id = random.randint(1, 3)
    speed = random.randint(20,200)
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().isoformat()
    

    return [surr_id, speed, date, time]


if __name__ == '__main__':   

    REST_API_URL = 'https://api.powerbi.com/beta/e4ee00ff-7efd-4d46-9b6a-9b41ea290be1/datasets/e78120bc-6a65-4059-84dc-77220ec93a52/rows?key=2PZdPDebYrov7xA9M6SOE%2BzO76UhgZBNvnW21nJhruyHnKPSuRuz4jCQbX9hbmEluMHJIWTeFcuq0cORAW1y2g%3D%3D'

    while True:
        data_raw = []
        for i in range(1):
            row = data_generation()
            data_raw.append(row)
            print("Raw data - ", data_raw)

        # set the header record
        HEADER = ["surr_id", "speed", "date", "time"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset", data_json)

        # Post the data on the Power BI API
        req = requests.post(REST_API_URL, data_json)

        print("Data posted in Power BI API")
        time.sleep(2)
