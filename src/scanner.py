import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator

stocks = {
    "RELIANCE": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "INFY": "INFY.NS",
    "SBI": "SBIN.NS",
    "HDFC": "HDFCBANK.NS",
    "ICICI": "ICICIBANK.NS",
    
}

results = []

for name, ticker in stocks.items():
    df = yf.download(ticker, period="3mo", interval="1d", progress=False)
    df.columns = df.columns.droplevel(1)

    rsi = RSIIndicator(df["Close"], window=14).rsi().iloc[-1]

    signal = "HOLD"
   if rsi < 30:
    signal = "🟢 STRONG BUY"
elif rsi < 40:
    signal = "🟢 BUY WATCH"
elif rsi <= 60:
    signal = "⚪ HOLD"
elif rsi <= 70:
    signal = "🟠 SELL WATCH"
else:
    signal = "🔴 STRONG SELL"

    results.append([name, round(rsi, 2), signal])

table = pd.DataFrame(results, columns=["Stock", "RSI", "Signal"])
table = table.sort_values("RSI")

print("\n===== FT_RSI SCANNER =====\n")
print(table.to_string(index=False))