import yfinance as yf
import pandas as pd
import streamlit as st
import re

# * Stock Exchange's Names 
stock_exchange_names = ['Bombay','Australia','Euronext','Frankfurt','FTSE','Johannesburg',
                        'Nasdaq','New York','Russell2000','Shanghai','Shenzhen','Taiwan',
                        'Tokyo','Toronto']

# * Sidebar DropDown SelectBox for Selecting Stock Exchanges
selected_stock_exchange = st.sidebar.selectbox(
    "Select A Stock Exchange To View Stocks List", stock_exchange_names
)

# * Getting Stocks Ticker, Company for Selected Stock Exchange
df = pd.read_csv(f"./data/{selected_stock_exchange}.csv")

# * Sidebar DropDown SelectBox for Selection Company
selected_ticker = st.sidebar.selectbox(
    "Select A Company to view Stock Data",
    df.Ticker.apply(lambda x: x.strip(" ")) + " - " + df.Company.apply(lambda x: x.strip(" "))
)
selected_ticker = selected_ticker.split(" - ")
ticker = selected_ticker[0]

st.write(f"""
# Stocks Tracking App
#### {selected_stock_exchange} Stock Exchange - {selected_ticker[1]} Stock Data
*NOTE: The Stock Price of Each Stock is the Currency where their Stock Exchange is Located Geographically*
""")
st.write("---")

# * Get Ticker Data from Yahoo Finance
tickerData = yf.Ticker(ticker)

# * Get Historical Data for Stock
tickerDf = tickerData.history(period='5Y')

st.subheader("Stock Closing Price Graph")
st.line_chart(tickerDf.Close)

st.write("---")

st.subheader("Stock Total Market Volume Graph")
st.line_chart(tickerDf.Volume)

# * Displaying Stock Related Information
tickerData = dict(tickerData.get_info())

stock_info = pd.DataFrame()
stock_info["Key"] = tickerData.keys()
stock_info["Value"] = tickerData.values()

stock_info["Key"] = stock_info["Key"].apply(lambda x: " ".join(re.split('(?=[A-Z])', x)).title())

stock_info.fillna("N/A", inplace=True)
stock_info["Value"] = stock_info["Value"].replace({"": "N/A"})
stock_info["Value"] = stock_info["Value"].apply(str)

st.write("---")
st.subheader("Stock Info")
col0, col1 = st.columns(2)
with col0:
    st.write(stock_info.iloc[:9, :])
with col1:
    st.write(stock_info.iloc[9:18, :])

col0, col1 = st.columns(2)
with col0:
    st.write(stock_info.iloc[18:27, :])
with col1:
    st.write(stock_info.iloc[27:36, :])
    
col0, col1 = st.columns(2)
with col0:
    st.write(stock_info.iloc[36:45, :])
with col1:
    st.write(stock_info.iloc[45:54, :])

col0, col1 = st.columns(2)
with col0:
    st.write(stock_info.iloc[36:45, :])
with col1:
    st.write(stock_info.iloc[45:54, :])
    
col0, col1 = st.columns(2)
with col0:
    st.write(stock_info.iloc[54:63, :])
with col1:
    st.write(stock_info.iloc[63:72, :])
    
col0, col1 = st.columns(2)
with col0:
    st.write(stock_info.iloc[72:81, :])
with col1:
    st.write(stock_info.iloc[81:90, :])
    
st.write(stock_info.iloc[90:, :])