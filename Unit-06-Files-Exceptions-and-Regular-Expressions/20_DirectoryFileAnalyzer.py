# ----------------------------------------------------
# Description:
# This program analyzes all files inside a directory.
# It counts the total files, calculates total size,
# and displays the number of files for each extension.
# ----------------------------------------------------

import os

folder = input("Enter folder path: ")

try:
    total_files = 0
    total_size = 0
    extensions = {}

    for root, folders, files in os.walk(folder):
        for file in files:
            total_files += 1

            path = os.path.join(root, file)
            total_size += os.path.getsize(path)

            extension = os.path.splitext(file)[1]

            if extension == "":
                extension = "No Extension"

            extensions[extension] = extensions.get(extension, 0) + 1

    print("\nDirectory Analysis")
    print("------------------")
    print("Total files:", total_files)
    print("Total size:", total_size, "bytes")

    print("\nFiles by extension:")
    for extension, count in extensions.items():
        print(extension, ":", count)

except FileNotFoundError:
    print("Folder not found.")

except PermissionError:
    print("Permission denied.")