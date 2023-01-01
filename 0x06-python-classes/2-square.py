#!/usr/bin/python3
'''
Module 1-square
Defines a square with private instance attribute
'''


class Square:
    '''
    square class with an attribute size

    Args:
        size: size of square
    '''

    def __init__(self, size=0):
        '''
        initialization of square class with size

        Attributes:
            size: size of square
        '''

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
