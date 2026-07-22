# ----------------------------------------------------
# Description:
# This program calculates the final amount
# after applying a discount.
# ----------------------------------------------------

price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = (price * discount) / 100
final_price = price - discount_amount

print(f"Discount Amount: {discount_amount:.2f}")
print(f"Final Price: {final_price:.2f}")