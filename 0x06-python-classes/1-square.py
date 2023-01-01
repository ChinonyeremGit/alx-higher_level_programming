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

    def __init__(self, size):
        '''
        initialization of square class with size

        Attributes:
            size: size of square
        '''

        self.__size = size
