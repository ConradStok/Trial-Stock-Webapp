import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
## OZMinerals Tracked over time

---

Stock closing price and volume:

""")

tickerSymbol = 'OZL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2018-1-1', end='2022-1-27')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDF.Volume)