import requests
import pandas as pd
import os

APIKEY = os.environ.get("APIKEY")


class DataStock:

    def __init__(self):
        self.parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": "IBM",
            "apikey": APIKEY
        }

        url = "https://www.alphavantage.co/query"

        self.response = requests.get(url, params=self.parameters)
        self.response.raise_for_status()
        self.data = self.response.json()
        self.latest_day = self.data["Time Series (Daily)"]

    def find_stock_days(self):
        stock_days = self.data["Time Series (Daily)"]
        df = pd.DataFrame(stock_days)
        latest_day = df.columns[0]
        previous_day = df.columns[1]
        last_two_days = [latest_day, previous_day]
        return last_two_days
