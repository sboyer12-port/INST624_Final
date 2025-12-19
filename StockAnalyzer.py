# Sebastian Boyer Final Project INST624
# Stock Analyzer

import sys
import matplotlib.pyplot as plt
from Analyzer import StockAnalyzer

API_KEY = "ASW4FSIWUW4Z009O" # this is my api key

if len(sys.argv) < 2:
    print("You forgot to add a stock symbol. Make sure to do that and try again.") # this code is just in case there isn't a stock symbol added.
    sys.exit(1)

symbol = sys.argv[1] # wrote this to take the first argument given in the terminal which will be the stock name, and then store it in "symbol"

analyzer = StockAnalyzer(symbol, API_KEY) # creating an object from the stock analyzer class that shows what stock and api key to use
analyzer.pulldata() # calling the pulldata method to make the request
df = analyzer.dataframe() # creating a pandas dataframe
stats = analyzer.analyze(df) # this method is to create/compile the statistics and then eventually return them as a dictionary


# so below I had to tweak several times. I didn't realize at first that I had to use specific variable names for the stats class and that was broken for a while
print(f"\nStock Analysis for {symbol}")
print(f"Average Close Price: ${stats['average_close']:2f}")
print(f"Highest Close Price: ${stats['max_close']:2f}")
print(f"Lowest Close Price: ${stats['min_close']:2f}")

# below is the creation of our graoh through myplotlib
plt.figure()
plt.plot(df.index, df["4. close"])
plt.title(f"{symbol} Closing Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price US")
plt.tight_layout()
plt.show()
