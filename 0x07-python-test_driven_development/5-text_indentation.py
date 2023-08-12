#!/usr/bin/python3
def text_indentation(text):
#Check if input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define the characters that will trigger the new lines
    newline_characters = ['.', '?', ':']

    # Initialize variables to keep track of the current line and the final output
    current_line = ""
    output = ""

    # Iterate through each character in the input text
    for char in text:
        # Check if the character is one of the newline trigger characters
        if char in newline_characters:
            # Append the current line to the output with 2 new lines
            output += current_line.strip() + "\n\n"
            # Reset the current line
            current_line = ""
        else:
            # Append the character to the current line
            current_line += char

    # Append the last line to the output
    output += current_line.strip()

    # Print the formatted output
    print(output)
