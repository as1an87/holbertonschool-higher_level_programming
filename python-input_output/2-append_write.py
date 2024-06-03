#!/usr/bin/python3
"""
readfile
"""


def append_write(filename="", text=""):
    """readfile"""
    char_count = len(text)
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
    return char_count
