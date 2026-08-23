# ----------------------------------------------------
# Description:
# This program reads a file and writes only the lines
# containing a user-specified keyword into another file.
# ----------------------------------------------------

source_file = input("Enter source file name: ")
output_file = input("Enter output file name: ")
keyword = input("Enter keyword to search: ").lower()

try:
    with open(source_file, "r") as source:
        lines = source.readlines()

    matching_lines = [
        line for line in lines
        if keyword in line.lower()
    ]

    with open(output_file, "w") as output:
        output.writelines(matching_lines)

    print(f"{len(matching_lines)} matching line(s) copied.")
    print("Output saved to:", output_file)

except FileNotFoundError:
    print("Source file not found.")