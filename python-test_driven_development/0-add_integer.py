#!/usr/bin/python3
"""
    Add integer
"""


def add_integer(a, b=98):
    """Add integer"""
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
