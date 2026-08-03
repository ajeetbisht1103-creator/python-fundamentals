# ----------------------------------------------------
# Description:
# This program stores daily expenses
# using a dictionary and calculates
# the total expenditure.
# ----------------------------------------------------

expenses = {}

n = int(input("Enter number of expense entries: "))

for i in range(n):
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    expenses[category] = amount

print("\nExpense Details")

total = 0

for category, amount in expenses.items():
    print(f"{category} : ₹{amount}")
    total += amount

print(f"\nTotal Expense: ₹{total}")