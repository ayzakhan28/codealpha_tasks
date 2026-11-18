
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

total_investment = 0
portfolio = []

while True:

    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    # Check whether stock exists
    if stock_name not in stock_prices:
        print("Stock not found! Please try again.")
        continue

    # Validate quantity
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            continue

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Calculate investment
    price = stock_prices[stock_name]
    investment = price * quantity

    total_investment += investment

    # Store stock details
    portfolio.append({
        "stock": stock_name,
        "price": price,
        "quantity": quantity,
        "investment": investment
    })

    print("\nStock:", stock_name)
    print("Price per share: $", price)
    print("Quantity:", quantity)
    print("Investment: $", investment)

# Display final portfolio
print("\n================================")
print("         YOUR PORTFOLIO")
print("================================")

for item in portfolio:
    print(
        item["stock"],
        "| Price: $", item["price"],
        "| Quantity:", item["quantity"],
        "| Investment: $", item["investment"]
    )

print("\nTotal Investment: $", total_investment)

# Save portfolio in text file
with open("portfolio.txt", "w", encoding="utf-8") as file:

    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("=======================\n\n")

    for item in portfolio:
        file.write(
            f"Stock: {item['stock']}\n"
            f"Price: ${item['price']}\n"
            f"Quantity: {item['quantity']}\n"
            f"Investment: ${item['investment']}\n\n"
        )

    file.write(f"Total Investment: ${total_investment}\n")

print("\nPortfolio saved successfully in portfolio.txt!")
print("Thank you for using Stock Portfolio Tracker!")
