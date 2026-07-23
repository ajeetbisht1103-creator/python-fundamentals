# ----------------------------------------------------
# Description:
# This program determines whether a transaction
# resulted in a profit, loss, or neither.
# ----------------------------------------------------

cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit: {profit:.2f}")

elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"Loss: {loss:.2f}")

else:
    print("No Profit, No Loss")