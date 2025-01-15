import ticker_search as ts
import alt_ticker_search as alt
import graph as g


def main():
    perform_search()


def perform_search():
    data = ts.load_json()
    ticker = ts.ticker_search(data)
    if ticker:
        stock_data = alt.get_stock_info(ticker)
        alt.print_stock_info(stock_data)



if __name__ == '__main__':
    main()
