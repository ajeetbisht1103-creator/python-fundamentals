# ----------------------------------------------------
# Description:
# This program reads a configuration file containing
# KEY=VALUE pairs, validates the syntax, and ignores
# comments (#) or empty lines. Valid entries are loaded
# into a dictionary.
# ----------------------------------------------------

import os

config_file = "config.env"


def parse_config(filepath):
    config = {}
    errors = 0

    try:
        with open(filepath, "r") as file:
            for line_no, line in enumerate(file, start=1):
                clean_line = line.strip()

                # Skip blank lines and comments
                if not clean_line or clean_line.startswith("#"):
                    continue

                if "=" in clean_line:
                    key, value = clean_line.split("=", 1)
                    key = key.strip()
                    value = value.strip()

                    if key:
                        config[key] = value
                    else:
                        print(f"Warning: Missing key on line {line_no}")
                        errors += 1
                else:
                    print(f"Warning: Invalid format on line {line_no}")
                    errors += 1

        return config, errors

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None, 0


# Execution
parsed_data, error_count = parse_config(config_file)

if parsed_data is not None:
    print("\n----- Parsed Configuration -----")
    for k, v in parsed_data.items():
        print(f"{k} -> {v}")
    print(f"\nParsing complete. Invalid lines: {error_count}")