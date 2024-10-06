import yfinance as yf
import pandas as pd
import datetime

# Define the stock ticker symbol (e.g. Apple Inc. is 'AAPL', S&P500 is '^GSPC')
ticker = "^GSPC"
# Get today's date
today = datetime.datetime.today().strftime('%Y-%m-%d')
# Download data for a specific period and interval
#data = yf.download(ticker, start="1928-01-01", end="2024-09-29", interval="1d")
data = yf.download(ticker, start="1928-01-01", end=today, interval="1d")

df = pd.DataFrame(data)
# Trimming specific columns to 2 decimal points
columns_to_trim = ['Open', 'Close', 'High', 'Low', 'Adj Close']
df[columns_to_trim] = df[columns_to_trim].round(2)

# Save to CSV
df.to_csv(f"{ticker}_historical_data.csv")