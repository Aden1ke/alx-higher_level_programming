#!/usr/bin/python3
""" function divs all element in the matrix"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix (list of lists): The matrix containing integers or floats.
        div (int or float): The number used for division.

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix or div is not the correct type.
        ZeroDivisionError: If div is 0.

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_length = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(row) != row_length:
                raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = round((element / div), 2)
            new_row.append(result)
            new_matrix.append(new_row)

    return new_matrix
