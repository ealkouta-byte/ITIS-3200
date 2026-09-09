# ITIS-3200 Lab 02 - Step 4 - Hashing Program
# Elian Alkoutami
# main.py

def main():
    # Ask the user for what they want to do
    print("1. Generate a new hash table")
    print("2. Verify hashes")
    choice = input("Enter your choice (1 or 2): ")

    # Print a message confirming selection, print an error message if the input is invalid
    if choice == "1":
        print("Generate hash table selected")
    elif choice == "2":
        print("Verify hashes selected")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

if __name__ == "__main__":
    main()