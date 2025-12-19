# Analyzer for replication as well

import requests # already downloaded through pip
import pandas as pd

class StockAnalyzer:
    def __init__(self, symbol, apikey): # these are the variable that I am going to mainly focusing on. Most important information of the stock
        self.symbol = symbol # creating my methods
        self.apikey = apikey
        self.data = None # null value for data
        
    def pulldata(self):
        url = "https://www.alphavantage.co/query" # this is the url we need to run our query. This is what will be ran through the terminal
        params = {
            "function": "TIME_SERIES_DAILY", # this is the function that we are returning from alpha vantage
            "symbol": self.symbol,
            "apikey": self.apikey
        }

        response = requests.get(url, params=params) # arguably the most important line in the program. This is sending our GET request to the API
        json_data = response.json() # this turns the response into a json response

        self.data = json_data["Time Series (Daily)"] # this is very important because it takes the daily stock price (I struggled with this too because I had to search to find the correct thing to write specifically for this variable)


        # below I am creating a method coverts the API data into a pandas DataFrame
    def dataframe(self):
        df = pd.DataFrame.from_dict(self.data, orient="index") # orient="index" is the way I found to appropriatly sort the data
        df = df.astype(float)
        df.index = pd.to_datetime(df.index)
        df.sort_index(inplace=True)
        return df 

        # for this below I also struggled for a while with the variable names
    def analyze(self, df):
        avg_close = df["4. close"].mean()
        max_close = df["4. close"].max()
        min_close = df["4. close"].min()

            # returns the program
        return {
        "average_close": avg_close,
        "max_close": max_close,
        "min_close": min_close
        }