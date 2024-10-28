# Lea Trueworthy
# September 29, 2024
# CSD 205 - Module 8.2 Assignment

# Description: Create a program with a dictionary of 10 fictional stock ticker symbols and prices that prompts the user for a symbol and displays its price or a not-found message.

# Dictionary of stock prices
stock_market = {
    'TSLA': 260.46,
    'AMZN': 187.97,
    'MSFT': 428.02,
    'GOOGL': 163.95,
    'AAPL': 227.73,
    'COST': 885.62,
    'BABA': 107,
    'SOFI': 8,
    'PFE': 29.09,
    'NFLX': 707.35
    }

# Prompt the user for a ticker symbol
search_ticker = input("Search for a company:")

# Search for the ticker symbol in the dictionary
if search_ticker in stock_market:
    stock_price = stock_market[search_ticker]
    print(f"The current price for {search_ticker} is ${stock_price}")
else:
    print("Ticker symbol", search_ticker, "is not found.")