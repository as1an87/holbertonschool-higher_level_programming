#!/usr/bin/python3
"""
classtojson
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, boolean)
    for JSON serialization of an object.

    Parameters:
    obj (object): An instance of a class.

    Returns:
    dict: A dictionary containing the serializable attributes of the object.
    """
    return obj.__dict__
