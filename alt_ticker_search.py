import json
import math
from numerize import numerize
import yfinance as yf

# List for simplifying large integers into more human-readable format
millnames = ['', ' Thousand ', ' Million', ' Billion ', ' Trillion ']


# Reads in the JSON file containing all the stock market tickers and company names
# Returns a dictionary with KV pairs where k = integer and v = cik_str, ticker, and title
def load_json():
    with open('stock_tickers.json', 'r') as file:
        data = json.load(file)
    return data


# Takes the dictionary from the load_json function and allows the user to locate a specific
# ticker given the company's full title. Will need to add functionality later so that the user can
# more simply perform the queries
def ticker_search(data) -> str:
    ticker = input("Enter Company Name:\n")

    for key, value in data.items():
        if value["title"] == ticker:
            print("Title located, returning ticker...")
            return value["ticker"]
    print("Ticker corresponding to title couldn't be found.")


def get_stock_info(ticker):
    ticker = yf.Ticker(ticker)
    return {
        "Market Cap": numerize.numerize(ticker.info.get('marketCap', 0), 2),
        "Revenue (ttm)": numerize.numerize(ticker.info.get('totalRevenue', 0), 2),
        "Net Income (ttm)": numerize.numerize(ticker.info.get('netIncomeToCommon', 0), 2),
        "Shares Outstanding": numerize.numerize(ticker.info.get('sharesOutstanding', 0), 2),
        "EPS (ttm)": numerize.numerize(ticker.info.get('trailingEps', 0), 2),
        "PE Ratio": numerize.numerize(ticker.info.get('trailingPE', 0), 2),
        "Forward PE": numerize.numerize(ticker.info.get('forwardPE', 0), 2),
        "Dividend": numerize.numerize(ticker.info.get('dividendRate', 0), 2),
        "Volume": ticker.info.get("volume", 0),
        "Open": ticker.info.get("open", 0),
        "Previous Close": ticker.info.get("previousClose", 0),
        "Beta": ticker.info.get("beta", 0),
        "Recommendation": ticker.info.get("recommendationKey", "N/A"),
        "Mean Price Target": ticker.info.get("targetMeanPrice", 0)
    }


def print_stock_info(data):
    print("Stock Information")
    print("-" * 30)
    for key, value in data.items():
        print(f"{key}: {value}")
    print("-" * 30)
