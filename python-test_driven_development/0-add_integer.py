#!/usr/bin/python3
"""
    Add integer
"""
def add_integer(a, b=98):
    """Add integer"""
    def cast_to_int(a, b):
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
        return a, b
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
