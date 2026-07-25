# ----------------------------------------------------
# Description:
# This program performs a basic validation
# of an email address.
# ----------------------------------------------------

email = input("Enter an email address: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid Email Address")
else:
    print("Invalid Email Address")