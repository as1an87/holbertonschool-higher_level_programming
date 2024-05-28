#!/usr/bin/python3
class Square:
    def __init__(self, size = 0):
        if  not isinstance(size, int):
            raise TypeError("size must be integer")
        self.__size = size
