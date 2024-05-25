#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element)
        new.append(new_row)
    for x in range(len(new)):
        for y in range(len(new)):
            new[x][y] = new[x][y] ** 2
    return new
