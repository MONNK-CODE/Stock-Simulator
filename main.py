# Install yfinance package for retrieving stock data
#pip install yfinance #will need to install this in bash if you're not using jupyter notebook

# Import the yfinance library to access stock information
import yfinance as yf

# Initialize a portfolio dictionary with an initial cash balance
portfolio = {
    "cash": 50000  # Starting cash balance in the portfolio
}

# Function to retrieve the latest stock price for a given stock symbol
def get_stock_price(symbol):
    try:
        # Create a Ticker object for the given symbol
        stock = yf.Ticker(symbol)
        # Get the closing price of the stock for the latest trading day
        return stock.history(period="1d")['Close'].iloc[0]
    except Exception as e:
        # Print an error message if there's an issue fetching the price
        print(f"Error fetching price for {symbol}: {e}")
        return None

# Function to buy a specific quantity of stock
def buy_stock(symbol, quantity):
    stock_price = get_stock_price(symbol)
    if stock_price is None:
        print("Invalid stock symbol.")
        return
    # Calculate the total cost for the purchase
    total_cost = stock_price * quantity
    # Check if there's enough cash in the portfolio to buy the stock
    if portfolio["cash"] >= total_cost:
        # Add the stock symbol to portfolio if it's not already there
        portfolio.setdefault(symbol, 0)
        # Deduct the purchase cost from cash balance
        portfolio["cash"] -= total_cost
        # Increase the quantity of stock owned in the portfolio
        portfolio[symbol] += quantity
        print(f"Bought {quantity} shares of {symbol} for ${total_cost:.2f}.")
    else:
        # Print a message if there aren't enough funds to buy the stock
        print("Insufficient funds to buy stock.")

# Function to sell a specific quantity of stock
def sell_stock(symbol, quantity):
    stock_price = get_stock_price(symbol)
    if stock_price is None:
        print("Invalid stock symbol.")
        return
    # Check if the portfolio contains enough shares of the stock to sell
    if symbol in portfolio and portfolio[symbol] >= quantity:
        # Calculate the total revenue from selling the stock
        total_cost = stock_price * quantity
        # Deduct the sold quantity from the stock holdings
        portfolio[symbol] -= quantity
        # Add the revenue to the cash balance
        portfolio["cash"] += total_cost
        print(f"Sold {quantity} shares of {symbol} for ${total_cost:.2f}.")
    else:
        # Print a message if there aren't enough shares to sell
        print("You do not have enough shares to sell.")

# Function to calculate the current total value of the portfolio
def calculate_portfolio_value():
    total_value = portfolio["cash"]  # Start with the cash balance
    # Loop through each stock in the portfolio to add their current value
    for symbol, quantity in portfolio.items():
        if symbol != "cash":
            stock_price = get_stock_price(symbol)
            if stock_price is not None:
                total_value += stock_price * quantity
    return total_value  # Return the computed total portfolio value

# Interactive menu for the stock market simulator
while True:
    # Display menu options
    print("\nStock Market Simulator Menu:")
    print("1. Buy Stock")
    print("2. Sell Stock")
    print("3. View Portfolio")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")

    # Buy stock option
    if choice == '1':
        symbol = input("Enter the stock symbol: ").upper()  # Convert symbol to uppercase
        quantity = int(input("Enter the quantity to buy: "))
        buy_stock(symbol, quantity)

    # Sell stock option
    elif choice == '2':
        symbol = input("Enter the stock symbol: ").upper()  # Convert symbol to uppercase
        quantity = int(input("Enter the quantity to sell: "))
        sell_stock(symbol, quantity)

    # View portfolio option
    elif choice == '3':
        portfolio_value = calculate_portfolio_value()  # Get the current portfolio value
        print("Current Portfolio Value: $", portfolio_value)
        print("Portfolio Breakdown:")
        for symbol, quantity in portfolio.items():
            if symbol != "cash":
                print(f"{symbol}: {quantity} shares")
        print("Cash: $", portfolio["cash"])

    # Exit the program
    elif choice == '4':
        print("Thank you for using the Stock Market Simulator!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please try again.")
