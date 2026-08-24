# ----------------------------------------------------
# Description:
# This program creates a backup copy of a text file
# using file handling and exception handling.
# ----------------------------------------------------

import os

source_file = input("Enter source file name: ")
backup_file = input("Enter backup file name: ")

try:
    if not os.path.exists(source_file):
        raise FileNotFoundError("Source file does not exist.")

    with open(source_file, "r") as source:
        content = source.read()

    with open(backup_file, "w") as backup:
        backup.write(content)

    print("Backup created successfully.")
    print("Backup file:", backup_file)

except FileNotFoundError as error:
    print("Error:", error)

except PermissionError:
    print("Permission denied while accessing the file.")

finally:
    print("Backup operation completed.")