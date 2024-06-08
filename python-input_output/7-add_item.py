#!/usr/bin/python3
import sys
import os

# Import the required functions
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing items if the file exists
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
