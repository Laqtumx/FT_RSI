import yfinance as yf
from ta.momentum import RSIIndicator

# NSE stock
ticker = "RELIANCE.NS"

# Download last 6 months of data
df = yf.download(ticker, period="6mo", interval="1d")

# Calculate RSI
df["RSI"] = RSIIndicator(df["Close"].squeeze(), window=14).rsi()

# Trading signals
df["Signal"] = "HOLD"
df.loc[df["RSI"] < 30, "Signal"] = "BUY"
df.loc[df["RSI"] > 70, "Signal"] = "SELL"

# Display latest rows
print(df[["Close", "RSI", "Signal"]].tail(15))