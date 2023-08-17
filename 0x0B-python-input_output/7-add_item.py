#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys

def main():
    # Load existing data from the file if it exists, or initialize an empty list
    try:
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []

    # Get command-line arguments and add them to the existing data
    new_items = sys.argv[1:]  # Exclude the script name
    existing_data.extend(new_items)

    # Save the updated data to the file
    save_to_json_file(existing_data, "add_item.json")
    print("Items added and saved successfully.")

if __name__ == "__main__":
    main()
