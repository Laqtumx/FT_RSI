from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator, MACD

def add_indicators(df):
    from src.indicators import add_indicators

df = add_indicators(df)
    df["EMA20"] = EMAIndicator(df["Close"], window=20).ema_indicator()
    df["EMA50"] = EMAIndicator(df["Close"], window=50).ema_indicator()

    macd = MACD(df["Close"])
    df["MACD"] = macd.macd()
    df["Signal"] = macd.macd_signal()

    return df
score = 50

if df["RSI"].iloc[-1] < 30:
    score += 20

if df["EMA20"].iloc[-1] > df["EMA50"].iloc[-1]:
    score += 15

if df["MACD"].iloc[-1] > df["Signal"].iloc[-1]:
    score += 15

st.metric("AI Confidence Score", f"{score}%")