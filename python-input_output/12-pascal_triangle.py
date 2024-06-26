#!/usr/bin/python3
"""
12
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Parameters:
    - n (int): The number of rows in the triangle.

    Returns:
    list: A list of lists representing Pascal's triangle.
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
