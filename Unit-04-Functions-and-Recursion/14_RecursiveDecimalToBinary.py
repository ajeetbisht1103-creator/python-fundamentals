# ----------------------------------------------------
# Description:
# This program converts a decimal number into
# binary representation using recursion.
# ----------------------------------------------------

def decimal_to_binary(number):
    if number < 2:
        return str(number)

    return decimal_to_binary(number // 2) + str(number % 2)


number = int(input("Enter a non-negative decimal number: "))

if number < 0:
    print("Please enter a non-negative number.")
else:
    print("Binary:", decimal_to_binary(number))