#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        row = list(map(lambda x: x**2, row))
        new.append(row)
    return new
