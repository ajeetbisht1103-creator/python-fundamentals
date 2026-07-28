# ----------------------------------------------------
# Description:
# This program checks whether one string
# is a rotation of another string.
#
# Example:
# ABCD
# CDAB
# Output: Rotation
# ----------------------------------------------------

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if len(string1) == len(string2) and string2 in (string1 + string1):
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")