#!/usr/bin/python3
'''
Module 1-square
Defines a square with private initance attribute, size and
public instance method, area.
'''


class Square:
    '''
    square class with an attribute size

    Args:
        size (int): size of square

    Functions:
        __init__(self, size=0)
        area(self)
    '''

    def __init__(self, size=0):
        '''
        initialization of square class with size

        Attributes:
            __size (int): size of square
        '''

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        function to calculate area of a square

        Returns:
            area
        '''

        return (self.__size) ** 2
