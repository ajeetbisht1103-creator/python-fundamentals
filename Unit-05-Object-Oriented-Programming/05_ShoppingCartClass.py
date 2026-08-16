# ----------------------------------------------------
# Description:
# This program demonstrates a shopping cart implemented
# using a class and object-oriented methods.
# ----------------------------------------------------

class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def calculate_total(self):
        total = 0

        for name, price in self.items:
            total += price

        return total

    def display_cart(self):
        print("\nShopping Cart")

        for name, price in self.items:
            print(f"{name} : ₹{price:.2f}")

        print("-" * 25)
        print(f"Total: ₹{self.calculate_total():.2f}")


cart = ShoppingCart()

n = int(input("Enter number of items: "))

for i in range(n):
    name = input("Enter item name: ")
    price = float(input("Enter item price: ₹"))

    cart.add_item(name, price)

cart.display_cart()