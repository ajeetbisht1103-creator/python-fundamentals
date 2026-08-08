# ----------------------------------------------------
# Description:
# This program uses separate functions to convert
# temperature between Celsius and Fahrenheit.
# ----------------------------------------------------

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


choice = input("Enter conversion (C-F or F-C): ").upper()
temperature = float(input("Enter temperature: "))

if choice == "C-F":
    result = celsius_to_fahrenheit(temperature)
    print(f"Temperature: {result:.2f} °F")

elif choice == "F-C":
    result = fahrenheit_to_celsius(temperature)
    print(f"Temperature: {result:.2f} °C")

else:
    print("Invalid conversion choice.")