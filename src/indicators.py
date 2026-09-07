from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator, MACD


def add_indicators(df):
    # RSI
    df["RSI"] = RSIIndicator(df["Close"], window=14).rsi()

    # Exponential Moving Averages
    df["EMA20"] = EMAIndicator(df["Close"], window=20).ema_indicator()
    df["EMA50"] = EMAIndicator(df["Close"], window=50).ema_indicator()

    # MACD
    macd = MACD(df["Close"])
    df["MACD"] = macd.macd()
    df["Signal"] = macd.macd_signal()

    return df