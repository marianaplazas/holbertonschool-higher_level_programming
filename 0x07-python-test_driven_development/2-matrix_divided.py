#!/usr/bin/python3
"""
this module is for divide a entire matrix
"""
def matrix_divided(matrix, div):
    """
    arguemts the matrix and the div
    """
    new_matrix = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for aux in row:
            if type(aux) is not int and type(aux) is not float:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
        result = list(map(lambda x: round(x / div, 2), row))
        new_matrix.append(result)
    return new_matrix
