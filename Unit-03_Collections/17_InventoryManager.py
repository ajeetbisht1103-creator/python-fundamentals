# ----------------------------------------------------
# Description:
# This program stores products and their
# quantities using a dictionary.
# ----------------------------------------------------

inventory = {}

n = int(input("Enter number of products: "))

for i in range(n):
    product = input("Product Name: ")
    quantity = int(input("Quantity: "))
    inventory[product] = quantity

print("\nInventory")

for product, quantity in inventory.items():
    print(f"{product} : {quantity}")