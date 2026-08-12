# ----------------------------------------------------
# Description:
# This program converts a decimal number into
# octal representation using recursion.
# ----------------------------------------------------

def decimal_to_octal(number):
    if number < 8:
        return str(number)

    return decimal_to_octal(number // 8) + str(number % 8)


number = int(input("Enter a non-negative decimal number: "))

if number < 0:
    print("Please enter a non-negative number.")
else:
    print("Octal:", decimal_to_octal(number))