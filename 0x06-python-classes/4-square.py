#!/usr/bin/python3
'''
Module 1-square
Defines a square with private instance attribute, size,
public instance method, area, and getter/setter.
'''


class Square:
    '''
    square class with an attribute size

    Args:
        size (int): size of square

    Functions:
        __init__(self, size=0)
        size(self)
        size(self, value)
        area(self)
    '''

    def __init__(self, size=0):
        '''
        initialization of square class with size

        Attributes:
            size (int): size of square
        '''

        self.size = size

    @property
    def size(self):
        '''
        Getter

        Returns:
            size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Setter

        Args:
            value: value to set size to
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''
        function to calculate area of a square

        Returns:
            area
        '''

        return (self.__size) ** 2
