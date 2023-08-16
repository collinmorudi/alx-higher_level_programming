#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix[row][col] = matrix[row][col] ** 2

    return new_matrix
