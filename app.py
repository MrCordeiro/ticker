import datetime
import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Jerónimo Martins for the last 180 days.
""")

DAYS_IN_HISTORY = 180

end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=DAYS_IN_HISTORY)

tickerSymbol = "JMT.LS"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period="1d", start=start_date, end=end_date)

# tickerDf columns are: Open, Hign, Low, Close, Volume, Dividends, Stock, Splits

st.write("## Closing price")
st.line_chart(tickerDf.Close)
st.write("## Volume")
st.line_chart(tickerDf.Volume)
