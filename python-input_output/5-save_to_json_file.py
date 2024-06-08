#!/usr/bin/python3
"""
save to json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Parameters:
    my_obj (object): The object to be serialized to JSON
    and written to the file.
    filename (str): The name of the file to write the JSON representation to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
