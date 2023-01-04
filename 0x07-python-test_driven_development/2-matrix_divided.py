#!/usr/bin/python3
'''
Module 2-matrix_divided

Divides all elemets of a list
'''


def matrix_divided(matrix, div):
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)
    if all(isinstance(ele, list) for ele in matrix) is not True:
        raise TypeError(msg)
    for ele in matrix:
        for i in ele:
            if type(i) not in [int, float, bool]:
                raise TypeError(msg)
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float, bool]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    for sub_list in matrix:
        new_list.append([round(i/div, 2) for i in sub_list])
    return new_list
