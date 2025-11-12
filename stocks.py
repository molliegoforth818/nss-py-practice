#dict of company data
ticker_symbols = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE": "General Electric",
}

#initailizing empty dict for total summary
purchases_by_company = {}

#list of tuples of purchase info
purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]
#func to list all stock purchases
def stock_purchases():
    print("List of all purchases")
    print("-------------------------")
    for ticker, shares, date, price in purchases:
        company_name = ticker_symbols.get(ticker)
        total_cost = shares * price
        print(f"{company_name} purchased {total_cost} on {date}")

#func to show total purchase summary

def total_summary():
    for purchase in purchases:
        ticker = purchase[0]
        if ticker in purchases_by_company:
            purchases_by_company[ticker].append(purchase)
        else:
            purchases_by_company[ticker] = [purchase] 
portfolio_total = 0
for ticker, purchases in purchases_by_company.items():
    total = 0
    for purchase in purchases:
        shares = purchase[1]
        price = purchase[3]
        total += shares * price
    portfolio_total += total
    print(f"* {ticker} Holdings: ${total}")

print("\nPortfolio Total")
print("----------------")
print(f"Total value of stock in portfolio: ${portfolio_total}")




stock_purchases()
total_summary()

