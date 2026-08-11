# ----------------------------------------------------
# Description:
# This program checks whether a string is a palindrome
# using recursion.
# ----------------------------------------------------

def is_palindrome(text, start, end):
    if start >= end:
        return True

    if text[start] != text[end]:
        return False

    return is_palindrome(text, start + 1, end - 1)


text = input("Enter a string: ").lower().replace(" ", "")

if is_palindrome(text, 0, len(text) - 1):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")