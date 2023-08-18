#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = [row[:] for row in matrix]  # Create a deep copy of the matrix
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            new_list[i][j] = new_list[i][j] ** 2
    return new_list[:]
