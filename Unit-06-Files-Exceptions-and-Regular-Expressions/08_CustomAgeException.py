# ----------------------------------------------------
# Description:
# This program demonstrates a user-defined exception
# for validating a person's age.
# ----------------------------------------------------

class InvalidAgeError(Exception):
    pass


def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")

    if age < 18:
        raise InvalidAgeError("Person must be at least 18 years old.")

    return True


try:
    age = int(input("Enter age: "))

    validate_age(age)

    print("Age is valid.")
    print("Person is eligible.")

except ValueError:
    print("Please enter a valid integer.")

except InvalidAgeError as error:
    print("Validation Error:", error)

finally:
    print("Age validation completed.")