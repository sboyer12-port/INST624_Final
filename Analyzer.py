# Analyzer for replication as well

import requests # already downloaded through pip
import pandas as pd

class StockAnalyzer:
    def __init__(self, symbol, apikey): # these are the variable that I am going to mainly focusing on. Most important information of the stock
        self.symbol = symbol # creating my methods
        self.apikey = apikey
        self.data = None # null value for data
        