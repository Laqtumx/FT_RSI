import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from src.indicators import add_indicators

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="FT_RSI Quantum Terminal",
    layout="wide"
)

st.title("⚡ FT_RSI Quantum Terminal")
st.caption("Built by Laqtumx • Quantitative Trading Dashboard")

# -----------------------------
# STOCK INPUT
# -----------------------------
ticker = st.text_input("NSE Ticker", "RELIANCE.NS")

# -----------------------------
# DOWNLOAD DATA
# -----------------------------
df = yf.download(ticker, period="6mo", interval="1d", progress=False)

# Fix multi-index columns
if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
    df.columns = df.columns.droplevel(1)

# Add RSI, EMA, MACD
df = add_indicators(df)

# -----------------------------
# PORTFOLIO SIMULATOR
# -----------------------------
initial_capital = 100000  # ₹1 Lakh

first_price = float(df["Close"].iloc[0])
last_price = float(df["Close"].iloc[-1])

shares = initial_capital / first_price
current_value = shares * last_price
profit = current_value - initial_capital
return_pct = (profit / initial_capital) * 100

# -----------------------------
# AI CONFIDENCE SCORE
# -----------------------------
score = 50

if df["RSI"].iloc[-1] < 30:
    score += 20

if df["EMA20"].iloc[-1] > df["EMA50"].iloc[-1]:
    score += 15

if df["MACD"].iloc[-1] > df["Signal"].iloc[-1]:
    score += 15

# -----------------------------
# KPI CARDS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💼 Portfolio Value",
        f"₹{current_value:,.0f}",
        f"{return_pct:.2f}%"
    )

with col2:
    st.metric(
        "💰 Profit / Loss",
        f"₹{profit:,.0f}",
        f"{profit:+,.0f}"
    )

with col3:
    st.metric(
        "🤖 AI Confidence",
        f"{score}%"
    )

# -----------------------------
# CANDLESTICK CHART
# -----------------------------
fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=df.index,
    open=df["Open"],
    high=df["High"],
    low=df["Low"],
    close=df["Close"],
    name="Price"
))

fig.update_layout(
    title=f"{ticker} • 6 Month Candlestick",
    template="plotly_dark",
    height=600,
    xaxis_rangeslider_visible=False
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# RSI STATUS
# -----------------------------
latest_rsi = float(df["RSI"].iloc[-1])

st.subheader("RSI Analysis")

if latest_rsi < 30:
    st.success(f"🟢 STRONG BUY • RSI {latest_rsi:.1f}")

elif latest_rsi > 70:
    st.error(f"🔴 STRONG SELL • RSI {latest_rsi:.1f}")

else:
    st.info(f"⚪ HOLD • RSI {latest_rsi:.1f}")

# -----------------------------
# RAW DATA
# -----------------------------
with st.expander("📊 View Market Data"):
    st.dataframe(df.tail(20), use_container_width=True)