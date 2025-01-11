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

    # Returns market cap in more readable format
    print(f"Market Cap: ${numerize.numerize(ticker.info['marketCap'], 2)}")

    # Returns TTM revenue
    # CURRENTLY THIS DOES NOT MATCH STOCK ANALYSIS, NEED TO FIGURE OUT WHY
    print(f"Revenue(ttm): ${numerize.numerize(ticker.info["totalRevenue"], 2)}")

    # Returns Net Income Common
    # CURRENTLY THIS DOES NOT MATCH STOCK ANALYSIS, NEED TO FIGURE OUT WHY
    print(f"Net Income(ttm): ${numerize.numerize(ticker.info["netIncomeToCommon"], 2)}")

    # Returns Shares Outstanding
    print(f"Shares Outstanding: ${numerize.numerize(ticker.info["sharesOutstanding"], 2)}")

    # Returns Earnings Per Share
    print(f"EPS(ttm): ${numerize.numerize(ticker.info["trailingEps"], 2)}")

    # Returns trailing PE Ratio
    print(f"PE Ratio: {numerize.numerize(ticker.info["trailingPE"], 2)}")

    # Returns Forward PE
    # CURRENTLY THIS DOES NOT MATCH STOCK ANALYSIS, NEED TO FIGURE OUT WHY
    print(f"Forward PE: {numerize.numerize(ticker.info["forwardPE"], 2)}")

    # Returns Dividend
    print(f"Dividend: ${numerize.numerize(ticker.info["dividendRate"], 2)}")

    # Returns Volume
    print(f"Volume: {ticker.info["volume"]:,}")

    # Returns Open
    print(f"Open: ${ticker.info["open"]}")

    # Returns Previous Close
    print(f"Previous Close: ${ticker.info["previousClose"]}")

    # Returns Day's Range

    # Returns 52 Week Range

    # Returns Beta
    print(f"Beta: ${ticker.info["beta"]}")

    # Returns Analysts
    recommendationKey = ticker.info["recommendationKey"]
    if recommendationKey == "buy":
        print(f"Recommendation: Buy")
    if recommendationKey == "strong_buy":
        print(f"Recommendation: Strong Buy")

    # Returns Price Target
    print(f"Mean Price Target: ${ticker.info["targetMeanPrice"]}")


    # Returns Earnings Date


