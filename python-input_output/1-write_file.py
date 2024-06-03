#!/usr/bin/python3
"""
readfile
"""


def write_file(filename="", text=""):
    """readfile"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
