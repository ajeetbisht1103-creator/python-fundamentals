# ----------------------------------------------------
# Description:
# This program demonstrates how to define and
# call a function with parameters and a return value.
# ----------------------------------------------------

def calculate_total(price, quantity):
    return price * quantity


price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = calculate_total(price, quantity)

print(f"Total Amount: ₹{total:.2f}")