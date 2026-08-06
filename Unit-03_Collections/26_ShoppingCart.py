# ----------------------------------------------------
# Description:
# This program simulates a shopping cart
# using a dictionary where the user can
# add items with their prices and the
# program calculates the total bill.
# ----------------------------------------------------

cart = {}

n = int(input("Enter number of items: "))

for i in range(n):
    item = input("Enter item name: ")
    price = float(input("Enter price: ₹"))
    cart[item] = price

print("\n----- Shopping Cart -----")

total = 0

for item, price in cart.items():
    print(f"{item} : ₹{price:.2f}")
    total += price

print("-------------------------")
print(f"Total Bill : ₹{total:.2f}")