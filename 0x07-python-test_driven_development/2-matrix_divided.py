#!/usr/bin/python3
"""Defines a matrix function"""


def matrix_divided(matrix, div):
    # Check if matrix is a list of lists of integers/floats
    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows have the same size
    row_lengths = [len(row) for row in matrix]
    if not all(length == row_lengths[0] for length in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform matrix division and rounding
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]
    
    return (new_matrix)
