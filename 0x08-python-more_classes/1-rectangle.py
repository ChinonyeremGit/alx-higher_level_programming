#!/usr/bin/python3
'''
Module 0-rectangle

Template for a class rectangle with some features
'''


class Rectangle:
    '''
    Class rectangle to encapsule the features of a rectangle

    Args:
        width (int): width of rectangle
        height (int): height of rectangle

    Functions:
        __init__(self, width=0, height=0)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    '''
    def __init__(self, width=0, height=0):
        '''
        initializer
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Getter
        Returns the width of a rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        setter
        sets width to a value
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            '''
            Getter
            Returns the height of a rectangle
            '''
            return self.__height

        @height.setter
        def height(self, value):
            '''
            setter
            sets height to a value
            '''
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
