#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            #print(uppercase_char, end="")
            result += uppercase_char
        else:
            #print(char, end="", "\n")
            result += char
    print(result)
