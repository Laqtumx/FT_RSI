import yfinance as yf
from ta.momentum import RSIIndicator
import plotly.graph_objects as go
from plotly.subplots import make_subplots

ticker = "RELIANCE.NS"

df = yf.download(ticker, period="6mo", interval="1d")
df.columns = df.columns.droplevel(1)

df["RSI"] = RSIIndicator(df["Close"], window=14).rsi()

fig = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True,
    vertical_spacing=0.05,
    row_heights=[0.7, 0.3]
)

fig.add_trace(
    go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        name="Price"
    ),
    row=1,
    col=1
)

fig.add_trace(
    go.Scatter(
        x=df.index,
        y=df["RSI"],
        line=dict(color="purple", width=2),
        name="RSI"
    ),
    row=2,
    col=1
)

fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)

fig.update_layout(
    title=f"{ticker} • FT_RSI Dashboard",
    xaxis_rangeslider_visible=False,
    template="plotly_dark",
    height=700
)

fig.show()