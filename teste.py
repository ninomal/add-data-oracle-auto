import re

# List of strings
strings = [
    "Hello, World!",
    "Python is great @2024",
    "Special characters: #, $, %, &",
    "Just text with no specials"
]

# Regular expression pattern to find special characters
pattern = r'[^a-zA-Z0-9\s]'

# Create a new list to store modified strings
modified_strings = []

# Iterate through each string in the list
for text in strings:
    # Replace special characters with '_'
    modified_text = re.sub(pattern, '_', text)
    modified_strings.append(modified_text)

# Print the modified strings
for original, modified in zip(strings, modified_strings):
    print(f"Original: {original}\nModified: {modified}\n")

