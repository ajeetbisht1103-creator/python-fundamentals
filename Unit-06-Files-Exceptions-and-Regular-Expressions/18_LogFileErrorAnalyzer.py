# ----------------------------------------------------
# Description:
# This program reads a log file, identifies lines
# containing ERROR or WARNING, and creates a separate
# report file containing the detected issues.
# ----------------------------------------------------

input_file = input("Enter log file name: ")
output_file = input("Enter report file name: ")

error_count = 0
warning_count = 0

try:
    with open(input_file, "r") as file:
        lines = file.readlines()

    with open(output_file, "w") as report:
        for line in lines:
            upper_line = line.upper()

            if "ERROR" in upper_line:
                error_count += 1
                report.write("ERROR: " + line)

            elif "WARNING" in upper_line:
                warning_count += 1
                report.write("WARNING: " + line)

        report.write("\n----- Summary -----\n")
        report.write(f"Total Errors: {error_count}\n")
        report.write(f"Total Warnings: {warning_count}\n")

    print("\nAnalysis completed.")
    print("Errors:", error_count)
    print("Warnings:", warning_count)
    print("Report saved to:", output_file)

except FileNotFoundError:
    print("Log file not found.")

except PermissionError:
    print("Permission denied while accessing the file.")

finally:
    print("Log analysis completed.")