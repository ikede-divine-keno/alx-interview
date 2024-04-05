#!/usr/bin/python3
""" 0. Rotate 2D Matrix
mandatory
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
Prototype: def rotate_2d_matrix(matrix): """


def rotate_2d_matrix(matrix):
    """ rotate_matrix_clockwise(matrix): """
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse the rows
    for row in matrix:
        row.reverse()
