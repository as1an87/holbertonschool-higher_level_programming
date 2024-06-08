#!/usr/bin/python3
"""
load from json file
"""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Parameters:
    filename (str): The name of the file containing the JSON string.

    Returns:
    object: A Python object corresponding to the JSON string in the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
