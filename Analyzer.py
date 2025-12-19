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
        paramaters = {
            "function": "TIME_SERIES_DAILY", # this is the function that we are returning from alpha vantage
            "symbol": self.symbol,
            "apikey": self.apikey
        }