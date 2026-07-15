# Program to find the remainder when divided by 2

number = int(input("Enter a number: "))

remainder = number % 2

print("Remainder =", remainder)

if remainder == 0:
    print("The number is Even")
else:
    print("The number is Odd")