#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last_digit = number % 10
        print("{}".format(last_digit), end="")
    else:
        last_digit = number % -10
        last_digit = -last_digit
        print("{}".format(last_digit), end="")
    return last_digit
