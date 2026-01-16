#python calculator


#gather user input
revenue = float(input("total revenue in €"))
cost = float(input("total cost in €"))


#calculate profit
profit = revenue - cost


#calculate margin
margin = (profit / revenue) * 100


#present data
print("\n--- Financial Summary ---")
print(f"Revenue: ${revenue:,.2f}")
print(f"Costs: ${cost:,.2f}")
print(f"Profit: ${profit:,.2f}")
print(f"Profit Margin: {margin:.1f}%")