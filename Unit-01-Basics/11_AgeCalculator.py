# ----------------------------------------------------
# Description:
# This program calculates a person's age
# based on their birth year.
# ----------------------------------------------------

from datetime import datetime

current_year = datetime.now().year
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year

print(f"You are {age} years old.")