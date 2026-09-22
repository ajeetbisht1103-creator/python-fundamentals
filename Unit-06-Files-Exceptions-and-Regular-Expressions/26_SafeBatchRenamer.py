# ----------------------------------------------------
# Description:
# This program renames all files with a given extension
# in a target directory by appending a custom prefix,
# handling permission errors and target file collisions safely.
# ----------------------------------------------------

import os

target_directory = input("Enter target folder path: ")
target_ext = input("Enter file extension to target (e.g., .txt): ").strip()
prefix = input("Enter prefix to append: ").strip()

if not target_ext.startswith("."):
    target_ext = "." + target_ext

try:
    if not os.path.exists(target_directory):
        raise FileNotFoundError("Directory does not exist.")

    files = os.listdir(target_directory)
    renamed_count = 0

    for filename in files:
        if filename.endswith(target_ext) and not filename.startswith(prefix):
            old_path = os.path.join(target_directory, filename)
            new_filename = f"{prefix}_{filename}"
            new_path = os.path.join(target_directory, new_filename)

            if os.path.exists(new_path):
                print(f"Skipping '{filename}': Target name already exists.")
                continue

            os.rename(old_path, new_path)
            renamed_count += 1
            print(f"Renamed: {filename} -> {new_filename}")

    print(f"\nBatch rename finished. Total files renamed: {renamed_count}")

except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError:
    print("Error: Access denied to target directory.")