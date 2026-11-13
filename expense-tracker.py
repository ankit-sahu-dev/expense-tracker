expenses = []


add_more = "yes"
while add_more == "yes":
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_category = input("Enter expense category: ")
    
    expense2 = {
    "name": expense_name,
    "amount": expense_amount,
    "category": expense_category
    }
    expenses.append(expense2)
    print(expenses)
    add_more = input("Do you want to add another expense(yes/no): ")
    if add_more == "no":
        break
    
total = 0

for expense in expenses:
    total += expense2["amount"]
print( "Your total: ",total)

category_totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

print("CATEGORY SUMMARY")

for category, amount in category_totals.items():
    print(category, ":", amount)