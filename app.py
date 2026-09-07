import streamlit as st
import yfinance as yf
from ta.momentum import RSIIndicator
import plotly.graph_objects as go

st.set_page_config(page_title="FT_RSI", layout="wide")

st.title("⚡ FT_RSI Quantum Terminal")
st.caption("Built by Laqtumx • Quantitative Trading Dashboard")

ticker = st.text_input("NSE Ticker", "RELIANCE.NS")

df = yf.download(ticker, period="6mo", interval="1d")
df.columns = df.columns.droplevel(1)

df["RSI"] = RSIIndicator(df["Close"], window=14).rsi()

fig = go.Figure(go.Candlestick(
    x=df.index,
    open=df["Open"],
    high=df["High"],
    low=df["Low"],
    close=df["Close"]
))

st.plotly_chart(fig, use_container_width=True)

rsi = df["RSI"].iloc[-1]

if rsi < 30:
    st.success(f"🟢 BUY SIGNAL | RSI {rsi:.1f}")
elif rsi > 70:
    st.error(f"🔴 SELL SIGNAL | RSI {rsi:.1f}")
else:
    st.info(f"⚪ HOLD | RSI {rsi:.1f}")