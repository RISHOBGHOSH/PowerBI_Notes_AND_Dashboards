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

    REST_API_URL = 'https://api.powerbi.com/beta/af7d8b6a-08ee-4d3a-92d2-cc04d0a62913/datasets/38573b0d-0b8f-4fb2-b047-dc1f625a9117/rows?key=ZGQFN4vznlNSidmTlRgJ64V%2BJln1wAaSRkvtUz7Hi9gDff%2FvQn%2BqKdcFGFrnqXXXwXsDP%2B%2FUuKvgjK%2BK0lo3vQ%3D%3D'

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
