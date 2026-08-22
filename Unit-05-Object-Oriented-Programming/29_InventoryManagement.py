# ----------------------------------------------------
# Description:
# This program implements a basic inventory management
# system using classes, objects, encapsulation and
# methods for adding and selling products.
# ----------------------------------------------------

class Product:

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.__quantity = quantity

    def restock(self, quantity):
        if quantity > 0:
            self.__quantity += quantity

    def sell(self, quantity):
        if quantity <= 0:
            print("Invalid quantity.")
        elif quantity > self.__quantity:
            print("Insufficient stock.")
        else:
            self.__quantity -= quantity
            print("Product sold successfully.")

    def display(self):
        print(f"\nID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ₹{self.price:.2f}")
        print(f"Available Stock: {self.__quantity}")


product_id = input("Enter product ID: ")
name = input("Enter product name: ")
price = float(input("Enter product price: ₹"))
quantity = int(input("Enter initial quantity: "))

product = Product(product_id, name, price, quantity)

product.display()

sold = int(input("\nEnter quantity to sell: "))
product.sell(sold)

product.display()

restock = int(input("\nEnter quantity to restock: "))
product.restock(restock)

product.display()