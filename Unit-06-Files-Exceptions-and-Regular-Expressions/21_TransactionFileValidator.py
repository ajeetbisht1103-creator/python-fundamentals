# ----------------------------------------------------
# Description:
# This program reads transaction records from a file.
# Each record contains:
# Transaction ID, Name, Amount
# It validates the records and separates valid and
# invalid transactions into different files.
# ----------------------------------------------------

import re

input_file = "transactions.txt"
valid_file = "valid_transactions.txt"
invalid_file = "invalid_transactions.txt"

try:
    with open(input_file, "r") as file:
        lines = file.readlines()

    valid = []
    invalid = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        parts = line.split(",")

        if len(parts) != 3:
            invalid.append(line)
            continue

        transaction_id, name, amount = parts

        if not re.fullmatch(r"T\d{4}", transaction_id):
            invalid.append(line)
            continue

        if not name.strip():
            invalid.append(line)
            continue

        try:
            amount = float(amount)

            if amount <= 0:
                invalid.append(line)
            else:
                valid.append(line)

        except ValueError:
            invalid.append(line)

    with open(valid_file, "w") as file:
        for line in valid:
            file.write(line + "\n")

    with open(invalid_file, "w") as file:
        for line in invalid:
            file.write(line + "\n")

    print("Validation completed.")
    print("Valid transactions:", len(valid))
    print("Invalid transactions:", len(invalid))

except FileNotFoundError:
    print("Transaction file not found.")