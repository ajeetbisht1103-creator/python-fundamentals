# ----------------------------------------------------
# Description:
# This program reads a large text file in specified line 
# chunks to prevent memory overload. It handles missing 
# file exceptions and tracks progress chunk by chunk.
# ----------------------------------------------------

def read_in_chunks(file_object, chunk_size=3):
    """Generator function to read a file chunk by chunk."""
    while True:
        chunk = [file_object.readline() for _ in range(chunk_size)]
        # Remove empty lines resulting from EOF
        chunk = [line for line in chunk if line]
        if not chunk:
            break
        yield chunk


filename = "large_dataset.txt"
chunk_number = 1

try:
    with open(filename, "r") as file:
        print(f"Reading '{filename}' in chunks...\n")
        for chunk in read_in_chunks(file, chunk_size=3):
            print(f"--- Chunk {chunk_number} ---")
            for line in chunk:
                print(line.strip())
            chunk_number += 1
            print()

    print("File streaming complete.")

except FileNotFoundError:
    print(f"Error: Target file '{filename}' does not exist.")
except IOError as e:
    print(f"I/O Error while processing file: {e}")