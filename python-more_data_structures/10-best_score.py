#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_score = 0
    for value in a_dictionary.values():
        if value > best_score:
            best_score = value
    return best_score
