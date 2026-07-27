# ----------------------------------------------------
# Description:
# This program converts a sentence
# into CamelCase format.
#
# Example:
# hello world python
# HelloWorldPython
# ----------------------------------------------------

sentence = input("Enter a sentence: ")

words = sentence.split()

camel_case = ""

for word in words:
    camel_case += word.capitalize()

print("CamelCase String:")
print(camel_case)