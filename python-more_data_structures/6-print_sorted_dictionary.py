#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    sorted_dict = {key: value for key, value in sorted(a_dictionary.items())}
    for key in sorted_dict:
        print("{}: {}".format(key, sorted_dict[key]))
