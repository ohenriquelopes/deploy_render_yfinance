import streamlit as st
import datetime
import pandas as pd
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

st.set_page_config(page_title='Stock Prediction App', page_icon="🧊", layout='wide')


st.markdown('''
# My Stocks
---
''')

# List of tickers
us_stock_tickers = [
    "AAPL",  # Apple Inc.
    "MSFT",  # Microsoft Corporation
    "AMZN",  # Amazon.com Inc.
    "GOOGL", # Alphabet Inc. (Google)
    "FB",    # Meta Platforms, Inc. (Facebook)
    "TSLA",  # Tesla, Inc.
    "BRK.B", # Berkshire Hathaway Inc.
    "JPM",   # JPMorgan Chase & Co.
    "V",     # Visa Inc.
    "JNJ",   # Johnson & Johnson
    "WMT",   # Walmart Inc.
    "PG",    # Procter & Gamble Company
    "MA",    # Mastercard Incorporated
    "NVDA",  # NVIDIA Corporation
    "DIS",   # The Walt Disney Company
    "UNH",   # UnitedHealth Group Incorporated
    "BAC",   # Bank of America Corporation
    "HD",    # The Home Depot, Inc.
    "PYPL",  # PayPal Holdings, Inc.
    "CMCSA", # Comcast Corporation
]

# Dropdown
selected_ticker = st.selectbox("Select a ticker", us_stock_tickers)

# Display
st.write(f"Selected ticker: {selected_ticker}")

def get_last_price(ticker_symbol):
    try:
        stock_data = yf.Ticker(ticker_symbol)
        last_price = stock_data.history(period='1d')['Close'].iloc[-1]
        return last_price
    except:
        return None


last_price = get_last_price(selected_ticker)

if last_price is not None:
    st.info(f"Last Price for {selected_ticker}: ${last_price:.2f}")
else:
    st.error("Error fetching data")

# Web scraping of Stock data
selected_keys = [
    "auditRisk",
    "boardRisk",
    "compensationRisk",
    "shareHolderRightsRisk",
    "overallRisk",
    "governanceEpochDate",
    "compensationAsOfEpochDate",
    "maxAge",
    "priceHint",
    "previousClose",
    "open",
    "dayLow",
    "dayHigh",
    "regularMarketPreviousClose",
    "regularMarketOpen",
    "regularMarketDayLow",
    "regularMarketDayHigh",
    "dividendRate",
    "dividendYield",
    "exDividendDate",
    "payoutRatio",
    "fiveYearAvgDividendYield",
    "beta",
    "trailingPE",
    "forwardPE",
    "volume",
    "regularMarketVolume",
    "averageVolume",
    "averageVolume10days",
    "averageDailyVolume10Day",
    "bid",
    "ask",
    "bidSize",
    "askSize",
    "marketCap",
    "fiftyTwoWeekLow",
    "fiftyTwoWeekHigh",
    "priceToSalesTrailing12Months",
    "fiftyDayAverage",
    "twoHundredDayAverage",
    "trailingAnnualDividendRate",
    "trailingAnnualDividendYield",
    "currency",
    "enterpriseValue",
    "profitMargins",
    "floatShares",
    "sharesOutstanding",
    "sharesShort",
    "sharesShortPriorMonth",
    "sharesShortPreviousMonthDate",
    "dateShortInterest",
    "sharesPercentSharesOut",
    "heldPercentInsiders",
    "heldPercentInstitutions",
    "shortRatio",
    "shortPercentOfFloat",
    "impliedSharesOutstanding",
    "bookValue",
    "priceToBook",
    "lastFiscalYearEnd",
    "nextFiscalYearEnd",
    "mostRecentQuarter",
    "earningsQuarterlyGrowth",
    "netIncomeToCommon",
    "trailingEps",
    "forwardEps",
    "pegRatio",
    "lastSplitFactor",
    "lastSplitDate",
    "enterpriseToRevenue",
    "enterpriseToEbitda",
    "52WeekChange",
    "SandP52WeekChange",
    "lastDividendValue",
    "lastDividendDate",
    "exchange",
    "quoteType",
    "symbol",
    "underlyingSymbol",
    "shortName",
    "longName",
    "firstTradeDateEpochUtc",
    "timeZoneFullName",
    "timeZoneShortName",
    "uuid",
    "messageBoardId",
    "gmtOffSetMilliseconds",
    "currentPrice",
    "targetHighPrice",
    "targetLowPrice",
    "targetMeanPrice",
    "targetMedianPrice",
    "recommendationMean",
    "recommendationKey",
    "numberOfAnalystOpinions",
    "totalCash",
    "totalCashPerShare",
    "ebitda",
    "totalDebt",
    "quickRatio",
    "currentRatio",
    "totalRevenue",
    "debtToEquity",
    "revenuePerShare",
    "returnOnAssets",
    "returnOnEquity",
    "freeCashflow",
    "operatingCashflow",
    "earningsGrowth",
    "revenueGrowth",
    "grossMargins",
    "ebitdaMargins",
    "operatingMargins",
    "financialCurrency",
    "trailingPegRatio"
]



# msft = yf.Ticker("MSFT")
# st.info(msft.info['longBusinessSummary'])

# st.info(msft.info['open'])


# st.info(selected_ticker.info[selected_keys])

# subset_dict = {key: original_dict[key] for key in selected_keys}
info_text = ""
for i in range(10):
    info_text += f"{++i}"
st.info(info_text)

# Inicialize uma string vazia para concatenar informações
# info_text = ""
#
# # Itere pelas chaves selecionadas e concatene as informações
# for key in selected_keys:
#     info_text += f"{key}: {selected_ticker[key]}\n"
#
# # Use st.info para exibir todas as informações em uma única chamada
# st.info(info_text)