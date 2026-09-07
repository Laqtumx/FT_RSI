# ⚡ FT_RSI Quantum Terminal

> AI-powered quantitative stock research platform built with Python, Streamlit & Plotly.

![Dashboard](assets/dashboard.png)

## 🚀 Features

- 📈 Live NSE stock analysis
- 🕯 Interactive candlestick charts
- 📊 RSI, EMA20, EMA50 & MACD
- 🤖 AI Confidence Score
- 💼 ₹100,000 Portfolio Simulator
- 🔍 Multi-stock AI Scanner
- ⚙ Modular architecture

## 🏗 Architecture

Market Data → Indicators → AI Engine → Portfolio → Streamlit UI

## 🛠 Tech Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Charts | Plotly |
| Data | yFinance |
| Indicators | ta |
| Processing | Pandas |
| Language | Python |

## ⚡ Installation

```bash
git clone https://github.com/Laqtumx/FT_RSI.git
cd FT_RSI

python -m venv .venv
source .venv/Scripts/activate

pip install -r requirements.txt
streamlit run app.py
```
