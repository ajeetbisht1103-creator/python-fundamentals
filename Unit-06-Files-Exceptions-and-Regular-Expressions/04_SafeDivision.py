# ----------------------------------------------------
# Description:
# This program demonstrates exception handling by
# safely performing division and handling invalid
# numeric input and division by zero.
# ----------------------------------------------------

try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    result = numerator / denominator

except ValueError:
    print("Invalid input. Please enter numbers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Result:", result)

finally:
    print("Division operation completed.")