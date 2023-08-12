#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int/float): The divisor for division.

    Returns:
        list of lists: A new matrix with elements divided by the divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   or if each row of the matrix doesn't have the same size,
                   or if the divisor is not a number (integer or float).
        ZeroDivisionError: If the divisor is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(val, (int, float)) for row in matrix for val in row):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Check if each row has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if divisor is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if divisor is not 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix
