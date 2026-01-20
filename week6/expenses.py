expense_records = []
category_totals = {}
unique_category = set()
expense_total = 0
expense_sort = []

print("==personal expense tracker==")
for i in range (1,6,1):
    category = input(f"expense {i} category: ")
    amount = float(input(f"cost of item {i}: "))
    date = input(f"date of purchase (YYYY-MM-DD) of item {i}: ")
    expense_records.append((category, amount, date))
    unique_category.add(category)
    expense_total += amount

for record in expense_records:
    category = record[0]
    if category in category_totals:
        category_totals[category] += record[1]
    else:
        category_totals[category] = record[1]

print("==overall spending summary==")
for record in expense_records:
    amount = record[1]
    expense_sort.append(amount)

expense_sort.sort()
print(f"total spending: {expense_total}")
print(f"lowest expense: {expense_sort[0]}")
print(f"highest expense: {expense_sort[-1]}")
print(f"average spending: {expense_total / len(expense_records)}")

print("==unique categories spent on==")
print(unique_category)
print(f"total unique categories: {len(unique_category)}")


print("==spending by category==")
print(category_totals)