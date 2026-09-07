import yfinance as yf
from ta.momentum import RSIIndicator
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Change this to any NSE stock
ticker = "TCS.NS"

# Download data
df = yf.download(ticker, period="6mo", interval="1d")
df.columns = df.columns.droplevel(1)

# RSI
df["RSI"] = RSIIndicator(df["Close"], window=14).rsi()

# Signals
buy = (df["RSI"] < 30) & (df["RSI"].shift(1) >= 30)
sell = (df["RSI"] > 70) & (df["RSI"].shift(1) <= 70)

# Dashboard
fig = make_subplots(
    rows=2, cols=1,
    shared_xaxes=True,
    row_heights=[0.7,0.3],
    vertical_spacing=0.05
)

# Candlestick
fig.add_trace(go.Candlestick(
    x=df.index,
    open=df["Open"],
    high=df["High"],
    low=df["Low"],
    close=df["Close"],
    name="Price"
), row=1, col=1)

# BUY markers
fig.add_trace(go.Scatter(
    x=df.index[buy],
    y=df["Low"][buy] * 0.995,
    mode="markers",
    marker=dict(symbol="triangle-up", size=14, color="lime"),
    name="BUY"
), row=1, col=1)

# SELL markers
fig.add_trace(go.Scatter(
    x=df.index[sell],
    y=df["High"][sell] * 1.005,
    mode="markers",
    marker=dict(symbol="triangle-down", size=14, color="red"),
    name="SELL"
), row=1, col=1)

# RSI line
fig.add_trace(go.Scatter(
    x=df.index,
    y=df["RSI"],
    line=dict(color="orange", width=2),
    name="RSI"
), row=2, col=1)

# RSI levels
fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)

fig.update_layout(
    title=f"FT_RSI v1.1 • {ticker}",
    template="plotly_dark",
    height=750,
    xaxis_rangeslider_visible=False
)

fig.show()