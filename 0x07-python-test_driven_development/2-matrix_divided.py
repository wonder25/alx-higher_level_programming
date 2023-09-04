#!usr/bin/python3
"""Divides all elements in a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements in a matrix

    Args:
        matrix (list): A list of lists of ints or floats
        div (int/ float): the divisor
    Raises:
        TypeError: if the matrix contains non-numbers
        TypeError: if the matrix contains rows of different sizes
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is 0
    Returns:
        a new matrix representing the result of the division
    """

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(message)

    if not all( isinstance(row, list) for row in matrix):
        raise TypeError(message)

    for i in matrix:
        for j in i:
            if not isinstance(j, (float, int)):
                raise TypeError(message)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    for row in matrix:
        divided_row = []
        for element in row:
            divided_row.append(round(element / div, 2))
        divided_matrix.append(divided_row)

    return divided_matrix
