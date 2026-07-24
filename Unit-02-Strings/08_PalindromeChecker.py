# ----------------------------------------------------
# Description:
# This program checks whether the
# entered string is a palindrome.
# ----------------------------------------------------

text = input("Enter a string: ").lower().replace(" ", "")

if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")