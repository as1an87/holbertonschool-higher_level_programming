#!/usr/bin/python3
"""
fromjsonstring
"""


import json

def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Parameters:
    my_str (str): A JSON-formatted string.

    Returns:
    object: A Python object corresponding to the JSON string.
    """
    return json.loads(my_str)
