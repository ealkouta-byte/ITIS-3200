import hashlib
import os
import json

# ITIS-3200 Lab 02 - Step 4 - Hashing Program
# Elian Alkoutami
# main.py

def hash_file(filepath):
    # Read the file in chunks so we don't load huge files into memory all at once
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def traverse_directory(directory):
    # Walk through the directory and hash every file that is found
    files_hashes = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            files_hashes[filepath] = hash_file(filepath)
    return files_hashes

def generate_table(directory):
    # Hash everything in the directory and save the results to a JSON file
    file_hashes = traverse_directory(directory)
    with open("hash_table.json", "w") as f:
        json.dump(file_hashes, f, indent=4)
    print("Hash table generated and saved to hash_table.json")

def validate_hash(directory):
    # Load the previously saved hash table
    with open("hash_table.json", "r") as f:
        old_hashes = json.load(f)

    # Recompute hashes for what's currently in the directory
    current_hashes = traverse_directory(directory)

    # Check every file that was in the old table
    for filepath, old_hash in old_hashes.items():
        if filepath not in current_hashes:
            print(f"{filepath} has been deleted")
        elif current_hashes[filepath] == old_hash:
            print(f"{filepath} hash is valid")
        else:
            print(f"{filepath} hash is invalid")

    # Check for anything new that wasn't in the old table
    for filepath in current_hashes:
        if filepath not in old_hashes:
            print(f"{filepath} is a new file")

def main():
    # Ask the user for what they want to do
    print("1. Generate a new hash table")
    print("2. Verify hashes")
    choice = input("Enter your choice (1 or 2): ")

    # Print a message confirming selection, print an error message if the input is invalid
    if choice == "1":
        directory = input("Enter the directory to hash: ")
        generate_table(directory)
    elif choice == "2":
        directory = input("Enter the directory to validate: ")
        validate_hash(directory)
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

if __name__ == "__main__":
    main()