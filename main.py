import ticker_search as ts


def main():
    perform_search()


def perform_search():
    data = ts.load_json()
    ticker = ts.ticker_search(data)
    if ticker:
        ts.get_stock_info(ticker)



if __name__ == '__main__':
    main()
