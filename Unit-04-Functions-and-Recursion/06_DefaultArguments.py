# ----------------------------------------------------
# Description:
# This program demonstrates the use of default
# arguments in Python functions.
# ----------------------------------------------------

def calculate_bill(price, quantity=1, discount=0):
    total = price * quantity
    discount_amount = total * discount / 100
    return total - discount_amount


price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

discount = float(input("Enter discount percentage (0 if none): "))

final_amount = calculate_bill(price, quantity, discount)

print(f"Final Bill: ₹{final_amount:.2f}")