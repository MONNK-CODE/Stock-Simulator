#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install yfinance
import yfinance as yf
portfolio = {
     "cash": 50000
}
def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        return stock.history(period = "1d")['Close'].iloc[0]
    except:
        return None
def buy_stock(symbol, quantity):
    stock_price = get_stock_price(symbol)
    if stock_price is None:
        print("Invalid stock symbol.")
        return
    total_cost = stock_price * quantity
    if portfolio["cash"] >= total_cost:
        portfolio.setdefault(symbol, 0)
        portfolio["cash"] -= total_cost
        portfolio[symbol] += quantity
        print(f"Bought {quantity} shares of symbol for ${total_cost:.2f}.")
    else:
        print("Insuffiecient funds to buy stock. ")
def sell_stock(symbol, quantity):
    stock_price = get_stock_price(symbol)
    if stock_price is None:
        print ("Invalid stock symbol")
        return
    if symbol in portfolio and portfolio[symbol] >= quantity:
        total_cost = stock_price * quantity
        portfolio[symbol] -= quantity
        portfolio["cash"] += total_cost
        print(f"Sold {quantity} share of symbol for ${total_cost:.2f}.")
    else:
        print("You do not have enough shares to sell. ")
def calculate_portfolio_value():
    total_value = portfolio["cash"]
    for symbol, quantity in portfolio.items():
        if symbol != "cash":
            stock_price = get_stock_price(symbol)
            if stock_price is not None:
                total_value += stock_price * quantity
            return total_value
#Interactive Usage
while True:
    print("\nStock Market Simulator Menu:")
    print("1. Buy Stock")
    print("2. Sell Stock")
    print("3. View Portfolio")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        symbol = input("Enter the stock symbol: ")
        quantity = int(input("Enter the quantity to buy: "))
        buy_stock(symbol, quantity)
    elif choice == '2':
        symbol = input("Enter the stock symbol: ")
        quantity = int(input("Enter the quantity to sell: "))
        sell_stock(symbol, quantity)
    elif choice == '3':
        portfolio_value =  calculate_portfolio_value()
        print("Current Portfolio Value: $", portfolio_value)
        print("Portfolio Breakdown:")
        for symbol, quantity in portfolio.items():
            if symbol != "cash":
                print(f"{symbol}: {quantity} shares")
        print("Cash: $", portfolio["cash"])
    elif choice == '4':
        print("Thank you for using the Stock Market Simulator!")
        break
    else:
        print("Invalid choice. Please try again.")

