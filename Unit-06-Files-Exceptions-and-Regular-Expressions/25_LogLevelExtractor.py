# ----------------------------------------------------
# Description:
# This program scans a system log file using regex to
# extract timestamps, log levels (INFO, WARN, ERROR),
# and messages, saving extracted errors to a structured log.
# ----------------------------------------------------

import re

log_file = "system.log"
output_file = "extracted_errors.txt"

# Pattern matching: [YYYY-MM-DD HH:MM:SS] LEVEL Message
log_pattern = r"^\[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\]\s(INFO|WARN|ERROR)\s-\s(.+)$"

try:
    with open(log_file, "r") as file:
        logs = file.readlines()

    extracted_errors = []

    for line in logs:
        match = re.match(log_pattern, line.strip())
        if match:
            timestamp, level, message = match.groups()
            if level == "ERROR":
                extracted_errors.append(
                    f"[{timestamp}] CRITICAL: {message}\n"
                )

    with open(output_file, "w") as out:
        out.writelines(extracted_errors)

    print(
        f"Extraction complete. Found {len(extracted_errors)} ERROR records."
    )

except FileNotFoundError:
    print(f"Error: '{log_file}' not found. Please create the file first.")