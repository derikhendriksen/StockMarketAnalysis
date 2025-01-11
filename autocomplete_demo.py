from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# Define stock tickers for autocomplete
stock_tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "META", "TSLA", "NVDA"]
stock_completer = WordCompleter(stock_tickers, ignore_case=True)

# Prompt the user with autocomplete suggestions
user_input = prompt("Search for a stock: ", completer=stock_completer)

print(f"You selected: {user_input}")
