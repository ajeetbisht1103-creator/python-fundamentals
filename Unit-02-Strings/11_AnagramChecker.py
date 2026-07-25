# ----------------------------------------------------
# Description:
# This program checks whether two strings
# are anagrams of each other.
# ----------------------------------------------------

string1 = input("Enter first string: ").replace(" ", "").lower()
string2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(string1) == sorted(string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")