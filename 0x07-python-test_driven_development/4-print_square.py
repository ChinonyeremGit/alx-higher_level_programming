#!/usr/bin/python3
'''
Module - 4-print_square

Module contains fuctions print_square to print a square.
'''


def print_square(size):
    '''
    Prints squaree with #'s given int size
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
