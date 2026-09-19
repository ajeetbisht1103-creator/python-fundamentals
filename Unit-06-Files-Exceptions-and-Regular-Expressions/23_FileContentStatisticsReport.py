# ----------------------------------------------------
# Description:
# This program reads a text file and generates a report
# containing the number of lines, words, characters,
# and the longest line in the file.
# ----------------------------------------------------

input_file = "input.txt"
report_file = "file_report.txt"

try:
    with open(input_file, "r") as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    character_count = sum(len(line.rstrip("\n")) for line in lines)

    if lines:
        longest_line = max(lines, key=len).strip()
    else:
        longest_line = "No content"

    with open(report_file, "w") as file:
        file.write("FILE CONTENT REPORT\n")
        file.write("-------------------\n")
        file.write(f"Lines: {line_count}\n")
        file.write(f"Words: {word_count}\n")
        file.write(f"Characters: {character_count}\n")
        file.write(f"Longest line: {longest_line}\n")

    print("Report generated successfully.")

except FileNotFoundError:
    print("Input file not found.")

except PermissionError:
    print("Permission denied.")